# Base image: official Python 3.10, slim variant (no unnecessary OS packages)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first — this layer is cached unless requirements change
COPY requirements.txt .

# Install Python dependencies (no cache saves image space)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app (main.py, model_train.py)
COPY . .

# Train the model at build time so the image is self-contained.
# (model/iris_rf.joblib is gitignored, so a fresh clone has no model file —
#  building it here means `docker build` works with no pre-step.)
RUN python model_train.py

# Expose the port the app listens on (documentation only — docker run -p maps it)
EXPOSE 8000

# Default command when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
