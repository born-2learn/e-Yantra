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
mA.start(75)
mB.start(75)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")
x = 48
y=True
while (1):
    if (ser.in_waiting > 0):
        read_val = ser.read()
        x = ord(read_val)
    if x==116:#t
        y=True

    if y:
        if x == 48:  # 0
            print("stop")
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.LOW)
            x = 122
            y=False

        elif x == 49:  # 1
            print("forward")
            GPIO.output(motorA1pin, GPIO.HIGH)
            GPIO.output(motorA2pin, GPIO.LOW)
            temp1 = 1
            x = 122
        elif x == 50:  # 2
            print("right")
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.HIGH)
            GPIO.output(motorA1pin, GPIO.HIGH)
            GPIO.output(motorA2pin, GPIO.LOW)
            temp1 = 1
            x = 122
        elif x == 51:  # 3
            print("left")
            GPIO.output(motorA1pin, GPIO.HIGH)
            GPIO.output(motorA2pin, GPIO.LOW)
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.HIGH)
            temp1 = 1
            x = 122

        elif x == 52:  # 4
            print("backward")
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.HIGH)
            temp1 = 0
            x = 'z'

    #elif x == 108:
    #   print("low")
    #  mA.ChangeDutyCycle(25)
    # x = 122

    elif x == 113:#q
        GPIO.cleanup()
        break
