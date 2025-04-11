# Use official Python image with compatible TensorFlow version
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Create SQLite database directory
RUN mkdir -p /app/db

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Expose the port
EXPOSE 8000

# Run the application
ENTRYPOINT ["/app/entrypoint.sh"]