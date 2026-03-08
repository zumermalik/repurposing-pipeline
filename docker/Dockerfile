# Use a slim Python 3.10 image as the base
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files
# and to ensure output is logged to the terminal immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for bioinformatics libraries (like RDKit)
RUN apt-get update && apt-get install -y \
    build-essential \
    libxrender1 \
    libxext6 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Set the default command to run the pipeline 
# (Can be overridden when running the container)
ENTRYPOINT ["python", "scripts/run_inference.py"]
CMD ["--disease", "DEMO_DISEASE_01"]
