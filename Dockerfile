# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade huggingface_hub sentence-transformers langchain langchain-huggingface langchain-community

# Expose the application port
EXPOSE 8080

# Command to run the app
CMD ["python3", "app.py"]
