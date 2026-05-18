# Start from official Ubuntu image
FROM ubuntu:22.04

# Who maintains this
LABEL maintainer="you@example.com"

# Run commands during build
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy files from your machine into the image
COPY app.py .

# Expose a port
EXPOSE 5000

# Command to run when container starts
CMD ["python3", "app.py"]
