import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#closing the warnings when you are compiling the code GPIO.setwarnings(False)

RUNNING = True

#defining the pins

green = 22

red = 17

blue = 27

#defining the pins as output

GPIO.setup(red, GPIO.OUT)

GPIO.setup(green, GPIO.OUT)

GPIO.setup(blue, GPIO.OUT)

#choosing a frequency for pwm

print("Testing led out, Press CTRL+C to exit")
try:
     print("set GIOP high")
     GPIO.output(blue, GPIO.HIGH)
     time.sleep(5)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("some error")

finally:
   print("clean up")
   GPIO.cleanup() # cleanup all GPIO