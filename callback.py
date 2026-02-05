import requests
from config import CALLBACK_ENABLED, CALLBACK_URL

def send_callback(payload: dict):
    if CALLBACK_ENABLED:
        try:
            requests.post(CALLBACK_URL, json=payload, timeout=3)
        except:
            pass
