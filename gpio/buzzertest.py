from gpiozero import Buzzer
from gpiozero import LED
from time import sleep

green = LED(17)
red = LED(27)
blue = LED(18)
buzzer = Buzzer(3)

def ledOn():
    red.on()
    sleep(2)
    red.off()
    blue.on()
    sleep(2)
    blue.off()
    green.on()
    sleep(2)
    green.off()

def ringBuzzer():
    buzzer.on()
    sleep(5)
    buzzer.off()
