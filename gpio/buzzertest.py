from gpiozero import Buzzer
from gpiozero import LED
from time import sleep


buzzer = Buzzer(17)

def ringBuzzer():
    buzzer.on()
    sleep(5)
    buzzer.off()
