# Voicing the Cheshire Cat

<img src="https://github.com/alessio-git21/voicing-the-cheshire-cat/assets/100300894/d5af6a17-4b1d-4db6-b346-e216c1e22061" alt="Alt text" width="300px" height="300px">

Voicing-the-Cheshire-Cat is a multi-container application that leverages the [Cheshire Cat AI](https://github.com/cheshire-cat-ai/core) project in combination with two custom Docker images for text-to-speech conversion and audio generation. It gives voice to a chatbot by allowing users to listen to its responses.

The [text-to-speech image](https://hub.docker.com/r/alessio21/text-to-speech) runs the SpeechT5 models inside: it takes any text as input and generates a numpy array representing the corresponding audio. Different speakers can be used.

The [audio generation image](https://hub.docker.com/r/alessio21/play-numpy-array) can generate audio from *any* numpy array that represents audio.

## Features

* **Modular Design**: The multi-container application is designed with modularity in mind, making it adaptable for use in various chatbot scenarios beyond the Cheshire Cat project.

* **No audio files stored anywhere**: The audio is generated "on the fly" without saving any audio files.

* **Multi-speaker**: Different speakers can be used to generate audio.

## Requirements

* Docker
* Pulseaudio running on your pc. [Here](https://hub.docker.com/r/alessio21/play-numpy-array) you can find how to install Pulseaudio in order to ensure that the container that generates the audio works properly.

## Quick start

* Clone the project

* *Before* launching the container, remember to start Pulseaudio.

* Open the command prompt, move to the project folder and run:

      docker compose up

* Once all services have been launched go to http://localhost:1865/admin and configure your favourite language model.
* Enable the **audio plugin** in the plugins dashboard.
* Chat with the Cat and listen to its answers!

**Voice selection**: if you want to change the voice, in the compose file there is the SPEAKER environment variable which can be set with one of the names of the speaker embeddings available in the "speaker_embedding" folder.

## How it works:

1. User sends the message to the Cat container.
2. The Cat's responses are forwarded to the text-to-speech container.
3. The text-to-speech container converts the response into an audio array.
4. The audio array is sent to the third container, allowing users to hear the chatbot's response.

## Limitations
Audios for responses that are too long will be truncated to the maximum input length accepted by the SpeechT5 model.

