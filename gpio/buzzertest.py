from gpiozero import Buzzer
from gpiozero import LED
from time import sleep

red = LED(2)
green = LED(3)
buzzer = Buzzer(17)

def ledOn():
    red.on()
    sleep(5)
    red.off()

def ringBuzzer():
    buzzer.on()
    sleep(5)
    buzzer.off()
