from gpiozero import Buzzer
from gpiozero import LED
from time import sleep

green = LED(18)
red = LED(17)
blue = LED(27)
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
