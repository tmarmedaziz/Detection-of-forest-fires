import Adafruit_DHT as AD
import time

DHT_SENSOR = AD.DHT11
DHT_PIN = 17

while True:
    humidity, temperature = AD.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);
