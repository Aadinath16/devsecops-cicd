# Use a lightweight, secure base image
FROM python:3.11-slim-bookworm

# Set secure working directory
WORKDIR /app

# Install dependencies first to leverage Docker caching layers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ ./app
COPY run.py .

# Expose the Flask port
EXPOSE 5000

# Run as a non-root user for DevSecOps best practices
RUN useradd -u 8888 appuser && chown -R appuser /app
USER appuser

CMD ["python", "run.py"]