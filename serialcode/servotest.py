import RPi.GPIO as GPIO
import time

arm = 13
grab = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(arm, GPIO.OUT)
GPIO.setup(grab, GPIO.OUT)

s1 = GPIO.PWM(arm, 50) # GPIO 17 for PWM with 50Hz
s2 = GPIO.PWM(grab, 50) # GPIO 17 for PWM with 50Hz

s1.start(2.5) # Initialization
s2.start(2.5)
try:
  while True:
    k=float(input('duty cycle'))
    s1.ChangeDutyCycle(k)
    s2.ChangeDutyCycle(k)



except KeyboardInterrupt:
  s1.stop()
  s2.stop()
  GPIO.cleanup()