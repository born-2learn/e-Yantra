import serial
from serial import Serial
ser = Serial('/dev/ttyUSB0', 9600)
while 1:
    if(ser.in_waiting >0):
        line = ser.readline()
        print('Accepted val')
        print(line)
        if(line=='1'):
            print('true')