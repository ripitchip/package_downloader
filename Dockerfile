# Use AlmaLinux 8 as the base image
FROM almalinux:8

# Install necessary packages
RUN yum update -y && \
    yum -y install yum-utils && \
    yum install -y python312 python3.12-pip git && \
    yum clean all

# Install FastAPI and Uvicorn in the virtual environment
RUN pip3.12 install --upgrade pip && \
    pip3.12 install "fastapi[standard]"

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Expose the port Uvicorn will run on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["fastapi", "run", "src/main.py"]

