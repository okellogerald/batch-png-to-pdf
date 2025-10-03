# PNG to PDF Merger (Dockerized)

This project provides a lightweight Dockerized tool to **merge multiple PNG files into a single PDF** without losing any image quality.  
It uses Python with `img2pdf` for **lossless embedding** of images into a PDF container.

---

## 📦 Project Structure

```
png_to_pdf_merger/
├── Dockerfile
├── requirements.txt
├── merge_pngs.py
├── docker-compose.yml
├── my_images/        # (Put your PNG files here)
└── my_pdf/           # (Merged PDF will be saved here)
```

---

## 🚀 How to Use

### 1. Place PNG Files
- Add your `.png` files into the `my_images/` folder.
- Files are merged **in sorted order** based on filename.

---

### 2. Build and Run

```bash
docker compose up --build
```

✅ This will:
- Build the Docker image.
- Mount your input and output folders.
- Merge the PNGs into a single PDF file.

The merged PDF will appear inside the `my_pdf/` folder.

---

### 3. Clean Up (Optional)

After running:

```bash
docker compose down
```

This will stop and remove the container cleanly.

---

## ⚙️ Configuration

You can customize the following settings inside `docker-compose.yml`:

| Environment Variable | Description |
|:----------------------|:------------|
| `INPUT_DIR`            | Folder inside container where PNG files are located (default: `/app/input`) |
| `OUTPUT_DIR`           | Folder inside container where merged PDF will be saved (default: `/app/output`) |
| `OUTPUT_FILENAME`      | Name of the output PDF file (default: `merged_output.pdf`) |

Example (in `docker-compose.yml`):
```yaml
environment:
  INPUT_DIR: /app/input
  OUTPUT_DIR: /app/output
  OUTPUT_FILENAME: merged_custom.pdf
```

---

## 🛠️ Dependencies

The container uses:

- Python
- img2pdf
- Pillow

All dependencies are installed automatically via `pip`.

---

## ✨ Features

- **Lossless merging:** No compression or quality loss.
- **Flexible input/output:** Customize paths and filename easily.
- **Simple setup:** One command build and run with Docker Compose.
- **Portable:** Runs anywhere Docker is available.
