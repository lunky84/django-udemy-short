
# syntax=docker/dockerfile:1

FROM python:3.11-bullseye

WORKDIR /workspace

# Install Git
RUN apt-get update && \
    apt-get install -y git

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the server
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8041", "--noreload"]