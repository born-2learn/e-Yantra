import RPi.GPIO as GPIO
import time
'''
colors[0]-->Red
colors[1]-->Green
colors[2]-->Blue
colors[3]-->Red+Green
'''
def ledColor(val):
        colors = [0xFF0000, 0x0000FF, 0x00FF00, 0xFF00FF]
        pins = {'pin_R': 11, 'pin_G': 12, 'pin_B': 13}  # pins is a dict

        GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
        for i in pins:
                GPIO.setup(pins[i], GPIO.OUT)  # Set pins' mode is output
                GPIO.output(pins[i], GPIO.HIGH)  # Set pins to high(+3.3V) to off led

        p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
        p_G = GPIO.PWM(pins['pin_G'], 2000)
        p_B = GPIO.PWM(pins['pin_B'], 2000)

        p_R.start(0)  # Initial duty Cycle = 0(leds off)
        p_G.start(0)
        p_B.start(0)

        def map(x, in_min, in_max, out_min, out_max):
                return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

        def setColor(col):  # For example : col = 0x112233
                R_val = (col & 0x110000) >> 16
                G_val = (col & 0x001100) >> 8
                B_val = (col & 0x000011) >> 0

                R_val = map(R_val, 0, 255, 0, 100)
                G_val = map(G_val, 0, 255, 0, 100)
                B_val = map(B_val, 0, 255, 0, 100)

                p_R.ChangeDutyCycle(100 - R_val)  # Change duty cycle
                p_G.ChangeDutyCycle(100 - G_val)
                p_B.ChangeDutyCycle(100 - B_val)

        try:
                if val=='r':
                        setColor(colors[0])
                        time.sleep(1)
                        setColor(colors[4])
                elif val=='g':
                        setColor(colors[1])
                        time.sleep(1)
                        setColor(colors[4])
                if val=='b':
                        setColor(colors[2])
                        time.sleep(1)
                        setColor(colors[4])
                if val=='y':
                        setColor(colors[3])
                        time.sleep(1)
                        setColor(colors[4])
        except KeyboardInterrupt:
                p_R.stop()
                p_G.stop()
                p_B.stop()
                for i in pins:
                        GPIO.output(pins[i], GPIO.HIGH)  # Turn off all leds
                GPIO.cleanup()