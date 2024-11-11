# Use Python 3.10 with Debian Buster as the base image
FROM python:3.10.6-buster

# Set the working directory in the container
WORKDIR /var/app

# Copy requirements.txt into the container
COPY ./requirements.txt /var/app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files into the container
COPY . /var/app

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
