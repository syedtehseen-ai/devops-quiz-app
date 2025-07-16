FROM python:3.11-slim

WORKDIR /app

COPY ./app ./app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Expose FASTAPI Port
EXPOSE 8000

# Run FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]