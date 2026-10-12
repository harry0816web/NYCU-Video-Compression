#!/usr/bin/env python3
"""Compare quantization-table scales using bitrate and reconstruction quality."""

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
from codec_parameters import HEADER, Q  # noqa: E402


DEFAULT_IMAGES = [ROOT / "lena_gray.png", ROOT / "mandril_gray.png"]
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "results" / "quantization"


def scaled_quantization_table(scale):
    if scale <= 0:
        raise ValueError("quantization scale must be positive")
    # Quantization steps must remain positive integers.  Scale 1.0 exactly
    # reproduces the course-provided table.
    return np.maximum(1.0, np.rint(Q * scale)).astype(np.float64)


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


def scale_tag(scale):
    return f"q{scale:g}".replace("-", "m").replace(".", "p")


def run_experiment(images, scales, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    original_encoder_q = encoder.Q
    original_decoder_q = decoder.Q

    try:
        for image_path in images:
            image_path = image_path.resolve()
            with Image.open(image_path) as image:
                width, height = image.size

            for scale in scales:
                q_table = scaled_quantization_table(scale)
                encoder.Q = q_table
                decoder.Q = q_table

                tag = scale_tag(scale)
                bitstream_path = output_dir / f"{image_path.stem}_{tag}.bin"
                reconstructed_path = output_dir / f"{image_path.stem}_{tag}.png"
                print(f"[quantization] {image_path.name}, Q scale={scale:g}", flush=True)

                encoder.encode(image_path, bitstream_path)
                decoder.decode(
                    bitstream_path,
                    reconstructed_path,
                    width=width,
                    height=height,
                )
                metrics = measure(image_path, reconstructed_path, bitstream_path)
                rows.append(
                    {
                        "image": image_path.name,
                        "q_scale": scale,
                        **metrics,
                    }
                )
    finally:
        encoder.Q = original_encoder_q
        decoder.Q = original_decoder_q

    csv_path = output_dir / "quantization_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("\nimage                 Q scale   BPP       PSNR (dB)   MSE")
    print("--------------------  --------  --------  ----------  ----------")
    for row in rows:
        psnr = "inf" if math.isinf(row["psnr_db"]) else f'{row["psnr_db"]:.6f}'
        print(
            f'{row["image"]:<20}  {row["q_scale"]:>8g}  '
            f'{row["bpp"]:>8.6f}  {psnr:>10}  {row["mse"]:>10.6f}'
        )
    print(f"\nCSV: {csv_path}")
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Compare scaled quantization tables using BPP and PSNR."
    )
    parser.add_argument(
        "images",
        nargs="*",
        type=Path,
        default=DEFAULT_IMAGES,
        help="input grayscale images (default: Lena and Mandril)",
    )
    parser.add_argument(
        "--scales",
        nargs="+",
        type=float,
        default=[0.5, 1.0, 2.0],
        help="positive multipliers applied to Q (default: 0.5 1 2)",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    run_experiment(args.images, args.scales, args.output_dir)


if __name__ == "__main__":
    main()
