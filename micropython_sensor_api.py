API_URL = "http:// 192.168.1.17:5000/data"

def send_to_api():
    temp, humidity, ldr = read_sensors()
    
    payload = {
        "temperature": temp,
        "humidity": humidity,
        "light": ldr
    }
    
    response = urequests.post(API_URL, headers={"Content-Type": "application/json"}, json=payload)
    print("Response API:", response.text)
    response.close()

while True:
    send_to_ubidots()
    send_to_api()
    time.sleep(10)
