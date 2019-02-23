import serial
from serial import Serial
ser = Serial('/dev/ttyUSB0', 9600)
while 1:
    if(ser.in_waiting >0):
        input = ser.read()

        input_number = char(input)

        print(input_number)
        #for i in range(0, 3):
