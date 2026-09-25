"""Export the horizontal intensity profile of a selected image strip.

This gives camera channel counts, not calibrated radiance or wavelength.
Usage: python analysis/extract_profile.py image.jpg output.csv --top 200 --bottom 260
"""

import argparse
import csv
from pathlib import Path

import numpy as np
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--top", type=int, required=True, help="First included image row")
    parser.add_argument("--bottom", type=int, required=True, help="First excluded image row")
    args = parser.parse_args()
    pixels = np.asarray(Image.open(args.image).convert("RGB"), dtype=np.float64)
    height, width, _ = pixels.shape
    if not (0 <= args.top < args.bottom <= height):
        parser.error(f"Expected 0 <= top < bottom <= image height {height}")
    profile = pixels[args.top:args.bottom].mean(axis=0)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["pixel_x", "red_count", "green_count", "blue_count"])
        for x in range(width):
            writer.writerow([x, *[f"{value:.3f}" for value in profile[x]]])
    print(f"Wrote {width} pixel columns from rows {args.top}:{args.bottom} to {args.output}")


if __name__ == "__main__":
    main()
