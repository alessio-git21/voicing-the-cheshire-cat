from cat.mad_hatter.decorators import hook
import requests

API_URL = "http://container_tts:1000/tts"

@hook  # default priority = 1
def before_cat_sends_message(message, cat):
    print(message["content"])
    #send the cat answer to container_tts for text-to-speech
    payload = {"text":message["content"]}
    resp = requests.post(API_URL, json=payload)
    

    return message