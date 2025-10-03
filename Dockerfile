FROM python:alpine

WORKDIR /app

COPY requirements.txt .
COPY merge_pngs.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "merge_pngs.py"]
