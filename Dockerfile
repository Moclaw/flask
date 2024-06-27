# Use a lightweight Python base image
FROM python:3.9-slim

# Set a working directory for the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose the port where Flask listens (typically 5000)
EXPOSE 5000

# Specify the command to execute when the container starts
CMD ["flask", "run"]
