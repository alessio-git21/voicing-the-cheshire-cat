import numpy as np
import os
import pyaudio
import time
from flask import Flask, request, jsonify
import threading

def play_audio(array):
    fs = 16000

    # Play the audio using pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    stream.write(array.tobytes())
    time.sleep(2)  # Add a short delay (adjust as needed)
    stream.stop_stream()
    stream.close()
    p.terminate()


app = Flask(__name__)
@app.route('/send_array', methods=['POST'])
def generate_audio():

    data = request.get_json(force=True)

    # Extract the input text from the request

    x = np.array(data['audio_array']).astype(np.float32)
    print("Array audio ricevuto dal container audio")

    #start the process
    thread = threading.Thread(target=play_audio, args=(x,))
    thread.start()

    result = {'audio': "done"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=2865)











#api_url = "http://container_tts:2865/get_array"


#response = requests.get(api_url)
#response.raise_for_status()  # Genera un'eccezione per errori HTTP
#data = response.json()
#x = np.array(data['audio_array']).astype(np.float32)
#print("Array ricevuto:", x.shape)
#fs = 16000 # Hz


# Play the audio using pyaudio
#p = pyaudio.PyAudio()
#stream = p.open(format=pyaudio.paFloat32,
#                channels=1,
#                rate=fs,
#                output=True)

#stream.write(x.tobytes())
#time.sleep(2)  # Add a short delay (adjust as needed)
#stream.stop_stream()
#stream.close()
#p.terminate()


