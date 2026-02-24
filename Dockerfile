# -------------------------------
# EcoMind Production Dockerfile
# -------------------------------

# 1️⃣ Base Image
FROM python:3.10-slim

# 2️⃣ Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Set Working Directory
WORKDIR /app

# 4️⃣ Install System Dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5️⃣ Copy Requirements First (for caching)
COPY requirements.txt .

# 6️⃣ Install Python Dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 7️⃣ Copy Project Files
COPY . .

# 8️⃣ Create Non-root User
RUN useradd -m appuser
USER appuser

# 9️⃣ Expose Port
EXPOSE 8000

# 🔟 Run FastAPI with Uvicorn
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
