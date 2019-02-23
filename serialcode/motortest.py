import RPi.GPIO as GPIO
from time import sleep

motorA1pin = 24
motorA2pin = 23
motorAenablePin = 25

motorB1pin = 17
motorB2pin = 27
motorBenablePin = 22

temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorA1pin, GPIO.OUT)
GPIO.setup(motorA2pin, GPIO.OUT)
GPIO.setup(motorAenablePin, GPIO.OUT)
GPIO.output(motorA1pin, GPIO.LOW)
GPIO.output(motorA2pin, GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorB1pin, GPIO.OUT)
GPIO.setup(motorB2pin, GPIO.OUT)
GPIO.setup(motorBenablePin, GPIO.OUT)
GPIO.output(motorB1pin, GPIO.LOW)
GPIO.output(motorB2pin, GPIO.LOW)

mA = GPIO.PWM(motorAenablePin, 1000)
mB = GPIO.PWM(motorBenablePin, 1000)
mA.start(25)
mB.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while (1):

    x = input()

    if x == 'r':
        print("run")
        if (temp1 == 1):
            GPIO.output(motorA1pin, GPIO.HIGH)
            GPIO.output(motorA2pin, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.HIGH)
            print("backward")
            x = 'z'


    elif x == 's':
        print("stop")
        GPIO.output(motorA1pin, GPIO.LOW)
        GPIO.output(motorA2pin, GPIO.LOW)
        x = 'z'

    elif x == 'f':
        print("forward")
        GPIO.output(motorA1pin, GPIO.HIGH)
        GPIO.output(motorA2pin, GPIO.LOW)
        temp1 = 1
        x = 'z'

    elif x == 'b':
        print("backward")
        GPIO.output(motorA1pin, GPIO.LOW)
        GPIO.output(motorA2pin, GPIO.HIGH)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        mA.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'm':
        print("medium")
        mA.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'h':
        print("high")
        mA.ChangeDutyCycle(75)
        x = 'z'


    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")