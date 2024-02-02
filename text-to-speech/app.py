import numpy as np
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech
from transformers import SpeechT5HifiGan
import torch
import os
import requests
from flask import Flask, request, jsonify


speaker = os.environ.get("SPEAKER","slt") # variable for custom speaker embedding

models_path = "/app/models"

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts", cache_dir=models_path)
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts",cache_dir=models_path)

vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan",cache_dir=models_path)


#load embedding
embedding_path = f"/app/speaker_embedding/{speaker}.npy"
embedding = np.load(embedding_path)
embedding = torch.tensor(embedding).unsqueeze(0)


print("Models and speaker embedding ready.")

def text_to_speech(text):
    inputs = processor(text=text, return_tensors="pt")

    #limit the input length
    input_ids = inputs["input_ids"]
    input_ids = input_ids[..., :model.config.max_text_positions]

    #generate speech
    speech = model.generate_speech(input_ids,embedding, vocoder=vocoder)
    print("------------------------------------------the audio array is ready------------------------------------------")

    #send the audio array
    API_URL =  "http://container_audio:2865/send_array"
    payload = {'audio_array': speech.numpy().tolist()}
    resp = requests.post(API_URL, json=payload)
    print(resp)
    

app = Flask(__name__)
@app.route('/tts', methods=['POST'])
def inference():
    
    data = request.get_json(force=True)

    # Extract the input text from the request
    cat_answer = data['cat_answer']

    text_to_speech(cat_answer)
    
    #return response
    result = {'tts': "send"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=1000)
