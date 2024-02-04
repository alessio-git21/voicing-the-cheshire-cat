# Voicing the Cheshire Cat

<img src="https://github.com/alessio-git21/voicing-the-cheshire-cat/assets/100300894/d5af6a17-4b1d-4db6-b346-e216c1e22061" alt="Alt text" width="300px" height="300px">

Voicing-the-Cheshire-Cat is a project that gives voice to the awesome [Cat AI assistant](https://github.com/cheshire-cat-ai/core), allowing users to interact with a chatbot and hear its responses. This project is powered by three Docker containers, including two custom docker images created for audio generation and text-to-speech conversion.

The *modular design* of the project is due to the use of these custom docker images which can be used to power any other vocal AI assistant!

The [audio generation image](https://hub.docker.com/r/alessio21/play-numpy-array) can generate audio from *any* numpy array that represents audio.

The [text-to-speech image](https://hub.docker.com/r/alessio21/text-to-speech) runs the SpeechT5 models inside: it takes any text as input and generates a numpy array representing the corresponding audio. Different speakers can be used.

## Features

* **Cheshire Cat Integration**: Voicing-the-Cat leverages the Cheshire Cat project, a famous Italian cat AI assistant, allowing users to interact with the chatbot.

* **Text-to-Speech Conversion**: The project includes two custom containers for generating audio from any numpy array and converting text to speech. This enables the chatbot to communicate audibly.

* **No audio files stored anywhere**: The audio is generated "on the fly" without the need to save any audio file.

* **Multi-speaker**: Different speakers can be used to generate audio.

* **Modular Design**: The multi-container application is designed with modularity in mind, making it adaptable for use in various chatbot scenarios beyond the Cheshire Cat project.

## Requirements

* Docker
* Pulseaudio running on your pc. [Here](https://hub.docker.com/r/alessio21/play-numpy-array) you can find how to install Pulseaudio in order to ensure that the container that generates the audio works correctly.

## Quick start

* Clone the project

* Open the command prompt, move to the project folder and run:

      docker compose up

* Once all services have been launched go to http://localhost:1865/admin and configure your favourite language model.
* Enable the **audio plugin** in the plugins tabs.
* Chat with the Cat and listen to its answers!

**Voice selection**: if you want to change the voice, in the compose file there is the SPEAKER environment variable which can be set with one of the names of the speaker embeddings available in the "speaker_embedding" folder.

## How it works:

1. Users send message to the cat container.
2. The cat's responses are forwarded to the text-to-speech container.
3. The text-to-speech container converts the response into an audio array.
4. The audio array is sent to the third container, allowing users to hear the chatbot's response.
