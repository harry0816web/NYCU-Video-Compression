#!/usr/bin/env python3
"""Compare zigzag and raster coefficient scans using bitrate and PSNR."""

import argparse
import csv
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import decoder  # noqa: E402
import encoder  # noqa: E402
from codec_parameters import HEADER, ZIGZAG  # noqa: E402


DEFAULT_IMAGES = [ROOT / "lena_gray.png", ROOT / "mandril_gray.png"]
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "results" / "scan_order"
SCAN_ORDERS = {
    "zigzag": ZIGZAG.copy(),
    "raster": np.arange(64, dtype=np.int32),
}


def measure(original_path, reconstructed_path, bitstream_path):
    original = np.asarray(Image.open(original_path).convert("L"), dtype=np.float64)
    reconstructed = np.asarray(
        Image.open(reconstructed_path).convert("L"), dtype=np.float64
    )
    if original.shape != reconstructed.shape:
        raise ValueError("image dimensions differ")

    mse = float(np.mean((original - reconstructed) ** 2))
    psnr = math.inf if mse == 0 else 10.0 * math.log10(255.0**2 / mse)
    data = bitstream_path.read_bytes()
    (payload_bits,) = HEADER.unpack(data[: HEADER.size])
    height, width = original.shape
    total_bits = len(data) * 8
    return {
        "payload_bits": payload_bits,
        "file_size_bytes": len(data),
        "bpp": total_bits / (height * width),
        "mse": mse,
        "psnr_db": psnr,
    }


def run_experiment(images, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    original_encoder_order = encoder.ZIGZAG
    original_decoder_order = decoder.ZIGZAG

    try:
        for image_path in images:
            image_path = image_path.resolve()
            with Image.open(image_path) as image:
                width, height = image.size

            for name, order in SCAN_ORDERS.items():
                # Both sides must use the same order.  The only changed
                # variable is how coefficients are arranged before EOB.
                encoder.ZIGZAG = order
                decoder.ZIGZAG = order

                bitstream_path = output_dir / f"{image_path.stem}_{name}.bin"
                reconstructed_path = output_dir / f"{image_path.stem}_{name}.png"
                print(f"[scan order] {image_path.name}, {name}", flush=True)

                encoder.encode(image_path, bitstream_path)
                decoder.decode(
                    bitstream_path,
                    reconstructed_path,
                    width=width,
                    height=height,
                )
                metrics = measure(image_path, reconstructed_path, bitstream_path)
                rows.append({"image": image_path.name, "scan_order": name, **metrics})
    finally:
        encoder.ZIGZAG = original_encoder_order
        decoder.ZIGZAG = original_decoder_order

    csv_path = output_dir / "scan_order_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("\nimage                 order    BPP       PSNR (dB)   MSE")
    print("--------------------  -------  --------  ----------  ----------")
    for row in rows:
        psnr = "inf" if math.isinf(row["psnr_db"]) else f'{row["psnr_db"]:.6f}'
        print(
            f'{row["image"]:<20}  {row["scan_order"]:<7}  '
            f'{row["bpp"]:>8.6f}  {psnr:>10}  {row["mse"]:>10.6f}'
        )
    print(f"\nCSV: {csv_path}")
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Compare zigzag and raster scans using BPP and PSNR."
    )
    parser.add_argument(
        "images",
        nargs="*",
        type=Path,
        default=DEFAULT_IMAGES,
        help="input grayscale images (default: Lena and Mandril)",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    run_experiment(args.images, args.output_dir)


if __name__ == "__main__":
    main()
