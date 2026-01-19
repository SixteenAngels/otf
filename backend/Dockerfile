FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Initialize database and start server
CMD ["sh", "-c", "python init_db.py && python -m uvicorn main:app --host 0.0.0.0 --port 8000"]
