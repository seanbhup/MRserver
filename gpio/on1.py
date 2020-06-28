import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

ledPin = 4

gpio.setup(ledPin, gpio.OUT)

gpio.output(ledPin, gpio.HIGH)
