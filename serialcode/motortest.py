import RPi.GPIO as GPIO
from gpiozero import Buzzer
from gpiozero import LED
from time import sleep
from serial import Serial

ser = Serial('/dev/ttyUSB0', 9600)

# LED pins
green = LED(16)
red = LED(20)
blue = LED(21)

motorA1pin = 17
motorA2pin = 27
motorAenablePin = 22

motorB1pin = 24
motorB2pin = 23
motorBenablePin = 25

arm = 13
grab = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(arm, GPIO.OUT)
GPIO.setup(grab, GPIO.OUT)

s1 = GPIO.PWM(arm, 50)  # GPIO 17 for PWM with 50Hz
s2 = GPIO.PWM(grab, 50)  # GPIO 17 for PWM with 50Hz

s1.start(6)  # Initialization
s2.start(3)

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
y = True


def ringBuzzer():
    buzzer = Buzzer(12)
    buzzer.on()
    sleep(5)
    buzzer.off()


led_var = False
while (1):
    if (ser.in_waiting > 0):
        read_val = ser.read()
        x = ord(read_val)

    if x == 98:
        ringBuzzer()
        break

    if x == 116:  # t
        y = True
    if y == False:
        if x == 55:  # 7
            s1.ChangeDutyCycle(4.5)
            sleep(1)
            s2.ChangeDutyCycle(5)
        elif x == 56:  # 8
            s1.ChangeDutyCycle(6)
            # s2.ChangeDutyCycle(k)
        elif x == 57:  # 9
            s1.ChangeDutyCycle(4.5)
            s2.ChangeDutyCycle(3)
        elif x == 114:  # red LED
            red.on()
        elif x == 103:  # green led
            green.on()
        elif x == 98:  # blue led
            blue.on()
        elif x == 121:  # yellow led
            red.on()
            green.on()
    if y:
        if x == 48:  # 0
            print("stop")
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.LOW)
            GPIO.output(motorB1pin, GPIO.LOW)
            GPIO.output(motorB2pin, GPIO.LOW)
            x = 122
            y = False

        elif x == 49:  # 1
            print("forward")
            GPIO.output(motorA1pin, GPIO.HIGH)
            GPIO.output(motorA2pin, GPIO.LOW)
            GPIO.output(motorB1pin, GPIO.HIGH)
            GPIO.output(motorB2pin, GPIO.LOW)
            temp1 = 1
            x = 122
        elif x == 50:  # 2
            print("right")
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.HIGH)
            GPIO.output(motorB1pin, GPIO.HIGH)
            GPIO.output(motorB2pin, GPIO.LOW)
            temp1 = 1
            x = 122
        elif x == 51:  # 3
            print("left")
            GPIO.output(motorA1pin, GPIO.HIGH)
            GPIO.output(motorA2pin, GPIO.LOW)
            GPIO.output(motorB1pin, GPIO.LOW)
            GPIO.output(motorB2pin, GPIO.HIGH)
            temp1 = 1
            x = 122

        elif x == 52:  # 4
            print("backward")
            GPIO.output(motorA1pin, GPIO.LOW)
            GPIO.output(motorA2pin, GPIO.HIGH)
            GPIO.output(motorB1pin, GPIO.LOW)
            GPIO.output(motorB2pin, GPIO.HIGH)
            temp1 = 0
            x = 'z'


    # elif x == 108:
    #   print("low")
    #  mA.ChangeDutyCycle(25)
    # x = 122

    elif x == 113:  # q

        s1.stop()
        s2.stop()
        GPIO.cleanup()
        break
