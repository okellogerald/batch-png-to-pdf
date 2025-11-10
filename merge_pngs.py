#!/usr/bin/env python3
import img2pdf
import os
from typing import Iterable, List

# ---- Configuration (via environment variables) ----
INPUT_DIR = os.getenv("INPUT_DIR", "./input")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")
OUTPUT_FILENAME = os.getenv("OUTPUT_FILENAME", "merged_output.pdf")

# File types we’ll accept as images
IMAGE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif", ".webp"
}


def natural_key(name: str) -> List:
    """
    Sort helper: 'page_2.png' comes before 'page_10.png'.
    Splits the filename into text + integer pieces.
    """
    import re

    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", name)
    ]


def find_image_files(directory: str) -> Iterable[str]:
    """Yield absolute paths of image files in `directory`."""
    with os.scandir(directory) as it:
        for entry in it:
            if not entry.is_file():
                continue
            _, ext = os.path.splitext(entry.name)
            if ext.lower() in IMAGE_EXTENSIONS:
                yield entry.path


def main() -> None:
    # Make sure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Collect and naturally sort image files
    image_files = sorted(find_image_files(INPUT_DIR),
                         key=lambda p: natural_key(os.path.basename(p)))

    if not image_files:
        raise ValueError(
            f"No image files found in {INPUT_DIR}. "
            f"Supported extensions: {', '.join(sorted(IMAGE_EXTENSIONS))}"
        )

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)

    # Convert & merge into a single PDF
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(image_files))

    print(f"✅ Successfully created PDF at: {output_path}")
    print(f"   Pages: {len(image_files)}")


if __name__ == "__main__":
    main()
