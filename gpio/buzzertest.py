from gpiozero import Buzzer
from gpiozero import LED
from time import sleep

red = LED(17)
blue = LED(27)
green = LED(4)
buzzer = Buzzer(3)

def ledOn():
    red.on()
    sleep(5)
    red.off()
    blue.on()
    sleep(5)
    blue.off()

def ringBuzzer():
    buzzer.on()
    sleep(5)
    buzzer.off()
