FROM python:3.10.6-buster: Uses Python 3.10 as the base image for the container.
WORKDIR /var/app: Sets the working directory for the container where your app files will be stored.
COPY ./requirements.txt /var/app: Copies the requirements.txt file from your local machine into the container.
RUN pip install --upgrade pip && pip install -r requirements.txt: Upgrades pip and installs all the dependencies listed in requirements.txt.
COPY . /var/app: Copies all the project files into the container.
CMD ["uvicorn", "app.main
", "--host", "0.0.0.0", "--port", "8000"]: Runs the FastAPI app using uvicorn as the server on port 8000.