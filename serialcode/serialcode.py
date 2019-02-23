import serial
from serial import Serial
ser = Serial('/dev/ttyUSB0', 9600)
while 1:
    if(ser.in_waiting >0):
        input = ser.read()

        input_number = ord(input)

        print("Read input back: " + str(input_number))
        #for i in range(0, 3):
