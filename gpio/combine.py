import buzzertest
import gpioled

for i in range(5):
    val=input('enter:')
    gpioled.ledColor(val)