# Voicing the Cheshire Cat

Voicing-the-Cheshire-Cat is a project that brings a voice to the famous [cat AI assistant](https://github.com/cheshire-cat-ai/core), allowing users to interact with a chatbot and hear its responses. This project is powered by three Docker containers, including two custom images created for audio generation and text-to-speech conversion.

The text-to-speech container runs the SpeechT5 models inside.

## Requirements

* Docker
* Pulseaudio server running on your pc. [Here](https://hub.docker.com/r/alessio21/play-numpy-array) you can find how to install pulseaudio in order to ensure that the container that generates the audio works correctly.

## Features

* **Cheshire Cat Integration**: Voicing-the-Cat leverages the Cheshire Cat project, a famous Italian cat AI assistant, allowing users to interact with the chatbot.

* **Text-to-Speech Conversion**: The project includes two custom containers for generating audio from any numpy array and converting text to speech. This enables the chatbot to communicate audibly.

* **No audio files stored anywhere**: The audio is generated "on the fly" without the need to save any audio file

* **Multi-speaker**: Different speakers can be used to generate audio

* **Modular Design**: The multi-container application is designed with modularity in mind, making it adaptable for use in various chatbot scenarios beyond the Cheshire Cat project.

## Quick start

* Run che docker compose file:

    docker-compose up

* Once all the service have been launched go to http://localhost:1865/admin and configure your favourite language model.
* Enable the **audio pluging** in the plugins tabs.
* Chat with the cat and listen to its answer!

## How it works:

* User send message to the cat container.
* The cat's responses are forwarded to the text-to-speech container.
* The text-to-speech container converts the response into an audio array.
* The audio array is sent to the third container, allowing users to hear the chatbot's response.
