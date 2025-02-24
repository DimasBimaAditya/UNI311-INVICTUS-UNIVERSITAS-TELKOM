import urequests
import ujson
import time
from sensor import read_sensors

TOKEN = "BBUS-eRs1BhPQEWGfD8vXZw3BrEeVKxRZdp"
DEVICE_LABEL = "sic-fix"
UBIDOTS_URL = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/"

HEADERS = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

def send_to_ubidots():
    temp, humidity, ldr = read_sensors()
    
    payload = {
        "temperature": temp,
        "humidity": humidity,
        "light": ldr
    }
    
    response = urequests.post(UBIDOTS_URL, headers=HEADERS, json=payload)
    print("Response:", response.text)
    response.close()

while True:
    send_to_ubidots()
    time.sleep(10)
