# Dockerfile
FROM python:3.12-slim

# Install system dependencies for torch‑geometric, ffmpeg, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git curl ca-certificates ffmpeg libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will use (Vercel provides $PORT)
EXPOSE 8501

# Use the PORT environment variable if set, otherwise default to 8501
CMD ["sh", "-c", "streamlit run ui/app.py --server.port ${PORT:-8501} --server.enableCORS false"]
