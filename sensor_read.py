import dht
import machine
import time


dht_sensor = dht.DHT11(machine.Pin(4))


ldr_pin = machine.ADC(machine.Pin(34))

def read_sensors():
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    
    ldr_value = ldr_pin.read()
    
    return temperature, humidity, ldr_value
