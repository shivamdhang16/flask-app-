# Use official Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port 6002
EXPOSE 6002

# Run the app
CMD ["python", "app.py"]

