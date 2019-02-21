import time, sys
import RPi.GPIO as GPIO

redPin = 2  # Set to appropriate GPIO
greenPin = 3  # Should be set in the
bluePin = 4  # GPIO.BOARD format


def blink(pin):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def redOn():
    blink(redPin)


def redOff():
    turnOff(redPin)


def greenOn():
    blink(greenPin)


def greenOff():
    turnOff(greenPin)


def blueOn():
    blink(bluePin)


def blueOff():
    turnOff(bluePin)


def yellowOn():
    blink(redPin)
    blink(greenPin)


def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)


def cyanOn():
    blink(greenPin)
    blink(bluePin)


def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)


def magentaOn():
    blink(redPin)
    blink(bluePin)


def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)


def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)


def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)


print("""Ensure the following GPIO connections: R-18, G-22, B-37
Colors: Red, Green, Blue, Yellow, Cyan, Magenta, and White
Use the format: color on/color off""")


def main():
    while True:
        cmd = raw_input("-->")