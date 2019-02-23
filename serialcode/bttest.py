import serial# library for serial   communication
import time     # for the timeout between messages

ser = serial.Serial (  "/dev/ttyAMA0", 9600 )
counter =  0
while  True :      # repeated loop until the program is interrupted
    counter = counter +  1
    ser.write ( str (counter) +  ' \ n ' )
    time.sleep ( 1 )                # wait for 1 second