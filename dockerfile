# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python app
COPY ankushmalgotra.py .

# Command to run the Python file
CMD ["python", "ankushmalgotra.py"]

