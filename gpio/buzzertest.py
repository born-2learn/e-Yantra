from gpiozero import Buzzer
from gpiozero import LED
from time import sleep


red = LED(17)
blue = LED(18)
green = LED()
buzzer = Buzzer(17)

def ringBuzzer():
    buzzer.on()
    sleep(5)
    buzzer.off()
