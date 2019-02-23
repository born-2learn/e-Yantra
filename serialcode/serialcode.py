
from serial import Serial
ser = Serial('/dev/ttyUSB0', 9600)
while 1:
    if(ser.in_waiting >0):
        input = ser.read()

        input_number = ord(input)

        if(input_number==49):
            print('true')
        #for i in range(0, 3):
