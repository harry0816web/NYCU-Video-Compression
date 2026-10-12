#!/usr/bin/env python3
"""Compare two-stage 1D DCT and direct double-summation 2D DCT."""

import argparse
import csv
import statistics
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import encoder  # noqa: E402
from codec_parameters import DCT_BASIS, HEADER, Q, ZIGZAG  # noqa: E402


DEFAULT_IMAGES = [ROOT / "lena_gray.png", ROOT / "mandril_gray.png"]
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "results" / "dct"


def two_stage_1d_dct(block, C=DCT_BASIS):
    after_rows = block @ C.T
    return C @ after_rows


def direct_2d_dct(block, C=DCT_BASIS):
    """Compute every coefficient with the required explicit double sum."""
    result = np.empty((8, 8), dtype=np.float64)
    for frequency_row in range(8):
        row_basis = C[frequency_row]
        for frequency_column in range(8):
            column_basis = C[frequency_column]
            coefficient = 0.0
            for spatial_row in range(8):
                row_weight = row_basis[spatial_row]
                for spatial_column in range(8):
                    coefficient += (
                        row_weight
                        * block[spatial_row, spatial_column]
                        * column_basis[spatial_column]
                    )
            result[frequency_row, frequency_column] = coefficient
    return result


def load_shifted_blocks(image_path):
    image = np.asarray(Image.open(image_path).convert("L"), dtype=np.float64)
    height, width = image.shape
    if height <= 0 or width <= 0 or height % 8 or width % 8:
        raise ValueError("image dimensions must be positive multiples of 8")
    return np.stack(
        [
            image[top : top + 8, left : left + 8] - 128.0
            for top in range(0, height, 8)
            for left in range(0, width, 8)
        ]
    )


def measure_dct(dct_function, blocks, repeats):
    # Warm-up is deliberately outside every timed interval.
    dct_function(blocks[0])
    timings = []
    for _ in range(repeats):
        start = time.perf_counter()
        for block in blocks:
            dct_function(block)
        timings.append(time.perf_counter() - start)
    return timings


def direct_transform_block(block, C=DCT_BASIS):
    """Encoder-compatible transform that changes only the DCT algorithm."""
    shifted = block.astype(np.float64) - 128.0
    dct_coefficients = direct_2d_dct(shifted, C)
    quantized = np.rint(dct_coefficients / Q).astype(np.int32)
    if np.any((quantized < -2047) | (quantized > 2047)):
        raise ValueError("quantized coefficient is outside supported range")
    scanned = quantized.flatten()[ZIGZAG]
    # No trace is requested in this experiment, so the row-stage value is
    # intentionally absent rather than performing extra unmeasured DCT work.
    return shifted, None, dct_coefficients, quantized, scanned


def bitstream_metrics(bitstream_path, width, height):
    data = bitstream_path.read_bytes()
    (payload_bits,) = HEADER.unpack(data[: HEADER.size])
    return {
        "payload_bits": payload_bits,
        "file_size_bytes": len(data),
        "bpp": len(data) * 8 / (width * height),
    }


def run_experiment(images, repeats, timing_block_limit, output_dir):
    if repeats <= 0:
        raise ValueError("repeats must be positive")
    if timing_block_limit < 0:
        raise ValueError("timing block limit cannot be negative")

    output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    standard_transform = encoder.transform_block

    try:
        for image_path in images:
            image_path = image_path.resolve()
            with Image.open(image_path) as image:
                width, height = image.size
            all_blocks = load_shifted_blocks(image_path)
            timed_blocks = (
                all_blocks[:timing_block_limit]
                if timing_block_limit
                else all_blocks
            )
            if len(timed_blocks) == 0:
                raise ValueError("no blocks selected for timing")

            # Catch matrix-direction or formula mistakes before timing.
            two_stage_first = two_stage_1d_dct(timed_blocks[0])
            direct_first = direct_2d_dct(timed_blocks[0])
            max_difference = float(np.max(np.abs(two_stage_first - direct_first)))
            if max_difference > 1e-9:
                raise AssertionError(
                    f"DCT implementations disagree: max difference={max_difference}"
                )

            method_data = [
                ("two_stage_1d", two_stage_1d_dct, standard_transform),
                ("direct_2d", direct_2d_dct, direct_transform_block),
            ]
            for method_name, dct_function, transform_function in method_data:
                print(
                    f"[DCT] {image_path.name}, {method_name}, "
                    f"{len(timed_blocks)} blocks x {repeats}",
                    flush=True,
                )
                timings = measure_dct(dct_function, timed_blocks, repeats)

                encoder.transform_block = transform_function
                bitstream_path = output_dir / f"{image_path.stem}_{method_name}.bin"
                encoder.encode(image_path, bitstream_path)
                metrics = bitstream_metrics(bitstream_path, width, height)
                rows.append(
                    {
                        "image": image_path.name,
                        "method": method_name,
                        "timed_blocks": len(timed_blocks),
                        "repeats": repeats,
                        "mean_dct_seconds": statistics.mean(timings),
                        "median_dct_seconds": statistics.median(timings),
                        "min_dct_seconds": min(timings),
                        **metrics,
                        "first_block_max_abs_difference": max_difference,
                    }
                )
    finally:
        encoder.transform_block = standard_transform

    csv_path = output_dir / "dct_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("\nimage                 method          median (s)   BPP")
    print("--------------------  --------------  -----------  --------")
    for row in rows:
        print(
            f'{row["image"]:<20}  {row["method"]:<14}  '
            f'{row["median_dct_seconds"]:>11.6f}  {row["bpp"]:>8.6f}'
        )
    print(f"\nCSV: {csv_path}")
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Compare two-stage 1D and explicit direct 2D DCT."
    )
    parser.add_argument(
        "images",
        nargs="*",
        type=Path,
        default=DEFAULT_IMAGES,
        help="input grayscale images (default: Lena and Mandril)",
    )
    parser.add_argument(
        "--repeats",
        type=int,
        default=3,
        help="timing repetitions after warm-up (default: 3)",
    )
    parser.add_argument(
        "--timing-block-limit",
        type=int,
        default=0,
        help="time only the first N blocks; 0 means all blocks",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    run_experiment(
        args.images,
        args.repeats,
        args.timing_block_limit,
        args.output_dir,
    )


if __name__ == "__main__":
    main()
