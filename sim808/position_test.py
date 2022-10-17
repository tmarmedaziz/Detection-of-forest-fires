import serial
import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BOARD)

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

port.write('AT+CGPSOUT=1\r\n'.encode())

rcv = port.read(1000)

print(rcv)

time.sleep(1)
