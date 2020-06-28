from gpiozero import LED
from time import sleep

led = LED(4)


def short(x):
    for i in range(x):
        led.on()
        sleep(.2)
        led.off()
        sleep(.2)

def long(x):
    for i in range(x):
        led.on()
        sleep(.5)
        led.off()
        sleep(.5)


short(3)
long(3)
short(3)



