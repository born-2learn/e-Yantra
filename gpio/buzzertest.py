from gpiozero import Buzzer
from gpiozero import LED
from time import sleep

green = LED(18)
red = LED(17)
blue = LED(27)
buzzer = Buzzer(3)


def ringBuzzer():
    buzzer.on()
    sleep(5)
    buzzer.off()
