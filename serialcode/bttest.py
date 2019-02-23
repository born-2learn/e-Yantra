import serial# library for serial   communication
import time     # for the timeout between messages

ser = serial.Serial (  "/dev/ttyAMA0", 9600 )
counter =  0
while  True :      # repeated loop until the program is interrupted
    if (ser.in_waiting() > 0):
        message = ser.read()
        print(message)
