import img2pdf
import os

# Environment variables with defaults
input_dir = os.getenv("INPUT_DIR", "./input")
output_dir = os.getenv("OUTPUT_DIR", "./output")
output_filename = os.getenv("OUTPUT_FILENAME", "merged_output.pdf")
output_path = os.path.join(output_dir, output_filename)

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# List and sort PNG files
png_files = sorted([
    os.path.join(input_dir, f)
    for f in os.listdir(input_dir)
    if f.lower().endswith(".png")
])

if not png_files:
    raise ValueError(f"No PNG files found in {input_dir}")

# Merge and save
with open(output_path, "wb") as f:
    f.write(img2pdf.convert(png_files))

print(f"✅ Successfully created PDF at {output_path}")
