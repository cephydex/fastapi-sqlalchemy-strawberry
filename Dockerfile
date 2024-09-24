FROM python:3.11-alpine

WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY .env .env

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:app" ]
CMD ["--host", "0.0.0.0", "--port", "8000", "--reload"]
