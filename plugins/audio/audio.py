from cat.mad_hatter.decorators import hook
import requests
import threading

API_URL = "http://container_tts:1000/tts"

@hook
def before_cat_sends_message(message, cat):
    print(message["content"])
    
    # Define a function to send the request in the background
    def send_request():
        payload = {"text": message["content"]}
        resp = requests.post(API_URL, json=payload)
        # You can process the response or perform other actions here if needed

    # Create a new thread and start it
    thread = threading.Thread(target=send_request)
    thread.start()

    # Return the original message to the user without waiting the audio to be synthesised
    return message
