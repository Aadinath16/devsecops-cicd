FROM python:3.11-slim-bookworm

WORKDIR /app

# SECURE FIX: Force upgrade global pip runtime tools to clear CVEs
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Now copy and install your app dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY run.py .

EXPOSE 5000

RUN useradd -u 8888 appuser && chown -R appuser /app
USER appuser

CMD ["python", "run.py"]