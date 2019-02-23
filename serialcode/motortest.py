import RPi.GPIO as GPIO
from time import sleep
from serial import Serial
ser = Serial('/dev/ttyUSB0', 9600)


motorA1pin = 17
motorA2pin = 27
motorAenablePin = 22

motorB1pin = 24
motorB2pin = 23
motorBenablePin = 25

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
x = 48
while (1):
    if (ser.in_waiting > 0):
        read_val = ser.read()
        x = ord(read_val)



    if x == 114:
        print("run")
        if (temp1 == 1):
            GPIO.output(motorA1pin, GPIO.HIGH)
            GPIO.output(motorA2pin, GPIO.LOW)
            print("forward")
            x = 122
        else:
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.HIGH)
            print("backward")
            x = 122


    elif x == 48:
        print("stop")
        GPIO.output(motorA1pin, GPIO.LOW)
        GPIO.output(motorA2pin, GPIO.LOW)
        x = 122

    elif x == 49:
        print("forward")
        GPIO.output(motorA1pin, GPIO.HIGH)
        GPIO.output(motorA2pin, GPIO.LOW)
        temp1 = 1
        x = 122

    elif x == 52:
        print("backward")
        GPIO.output(motorA1pin, GPIO.LOW)
        GPIO.output(motorA2pin, GPIO.HIGH)
        temp1 = 0
        x = 'z'

    elif x == 108:
        print("low")
        mA.ChangeDutyCycle(25)
        x = 122

    elif x == 109:
        print("medium")
        mA.ChangeDutyCycle(50)
        x = 122

    elif x == 104:
        print("high")
        mA.ChangeDutyCycle(75)
        x = 122


    elif x == 113:
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")