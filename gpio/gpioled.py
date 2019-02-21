import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#closing the warnings when you are compiling the code GPIO.setwarnings(False)

RUNNING = True

#defining the pins

green = 15

red = 11

blue = 13

#defining the pins as output

GPIO.setup(red, GPIO.OUT)

GPIO.setup(green, GPIO.OUT)

GPIO.setup(blue, GPIO.OUT)

#choosing a frequency for pwm

Freq = 100

#defining the pins that are going to be used with PWM

RED = GPIO.PWM(red, Freq)

GREEN = GPIO.PWM(green, Freq)

BLUE = GPIO.PWM(blue, Freq)

try:
    while RUNNING:
        # lighting up the pins. 100 means giving 100% to the pin

        RED.start(100)

        GREEN.start(1)

        BLUE.start(1)

        # For anode RGB LED users, if you want to start with RED too the only thing to be done is defining RED as one and GREEN and BLUE as 100.

        for x in range(1, 101):

        # for changing the width of PWM, this command is used

        GREEN.ChangeDutyCycle(x)

        # for anode LED users, just change x with 101-x

        # and for delay time.sleep is used. You can chance the duration of the colors with changing the time from here

        time.sleep(0.05)

        for x in range(1, 101):
            RED.ChangeDutyCycle(101 - x)
            time.sleep(0.025)




        for x in range(1, 101):
            GREEN.ChangeDutyCycle(101 - x)

            BLUE.ChangeDutyCycle(x)

            time.sleep(0.025)



        for x in range(1, 101):
            RED.ChangeDutyCycle(x)

            time.sleep(0.025)









except KeyboardInterrupt:
    RUNNING = False

    GPIO.cleanup()

#the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore

