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



#connect (position1, position2) on breadboard
#led (anode f1, cathode f4)
#22resistor (i1, -9)
#gpio 7 -->  j1
#gpio ground --> -1 



