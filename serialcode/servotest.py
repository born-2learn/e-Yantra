import RPi.GPIO as GPIO
import time

arm = 13
grab = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(arm, GPIO.OUT)
GPIO.setup(grab, GPIO.OUT)

s1 = GPIO.PWM(arm, 50) # GPIO 17 for PWM with 50Hz
s2 = GPIO.PWM(grab, 50) # GPIO 17 for PWM with 50Hz

s1.start(6) # Initialization
s2.start(5)
try:
  while True:

    k=input('duty cycle')
    if k=='7':

      s1.ChangeDutyCycle(4.5)
      s2.ChangeDutyCycle(5)
    if k == '8':
      s1.ChangeDutyCycle(6)
      #s2.ChangeDutyCycle(k)
    if k == '9':
      s1.ChangeDutyCycle(4.5)
      s2.ChangeDutyCycle(3)



except KeyboardInterrupt:
  s1.stop()
  s2.stop()
  GPIO.cleanup()