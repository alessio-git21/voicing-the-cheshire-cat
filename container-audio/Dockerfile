# Usa un'immagine di base con Python
FROM alpine

#install package for audio
RUN apk add --no-cache bash pulseaudio alsa-utils alsa-plugins-pulse

#install python
RUN apk add python3 py3-pip

#install required python packages
RUN apk add py3-numpy py3-pyaudio py3-flask

WORKDIR /app

COPY . /app

# Expose the port that the application listens on.
EXPOSE 2865

ENV PULSE_SERVER=host.docker.internal

CMD python3 audio.py

