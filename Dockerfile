FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 80 (standard for containerized deployments)
EXPOSE 80

# Use array syntax for CMD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
