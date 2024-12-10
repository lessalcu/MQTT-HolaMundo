# Base image
FROM python:3.9-slim

# Install dependencies
RUN pip install flask flask-restful flasgger paho-mqtt

# Copy files into the container
COPY app.py /app/app.py
COPY swagger.yaml /app/swagger.yaml

# Set working directory
WORKDIR /app

# Expose Flask port
EXPOSE 5000

# Default command
CMD ["python", "app.py"]