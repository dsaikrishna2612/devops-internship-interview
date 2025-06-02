# Use the official lightweight Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy only requirements file if you have one (optional optimization step)
# COPY requirements.txt .

# Install Flask (you can use requirements.txt if you have multiple dependencies)
RUN pip install --no-cache-dir flask

# Copy the entire app directory
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
