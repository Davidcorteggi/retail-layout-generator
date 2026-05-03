# Dockerfile
FROM python:3.12-slim

# Install system deps for torch‑geometric, ffmpeg, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git curl ca-certificates ffmpeg libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
CMD ["streamlit", "run", "ui/app.py", "--server.port", "8501", "--server.enableCORS", "false"]
