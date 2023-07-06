# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:latest

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Update OS and install common dev tools
RUN apt-get update
RUN apt-get install pulseaudio wget vim git zip unzip zlib1g-dev libzip-dev ffmpeg libpng-dev libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev python3-pyaudio -y
RUN pip install pyaudio

RUN pulseaudio -nC
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser