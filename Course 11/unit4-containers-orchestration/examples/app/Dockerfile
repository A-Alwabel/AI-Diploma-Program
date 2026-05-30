# Base image: official Python 3.10, slim variant (no unnecessary OS packages)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first — this layer is cached unless requirements change
COPY requirements.txt .

# Install Python dependencies (no cache saves image space)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app (model files, main.py)
COPY . .

# Expose the port the app listens on (documentation only — docker run -p maps it)
EXPOSE 8000

# Default command when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
