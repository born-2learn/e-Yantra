import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
import imutils
from serial import Serial
from gpiozero import Buzzer
from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO

ser = Serial('/dev/ttyUSB0', 9600)


def ringBuzzer():
    buzzer = Buzzer(3)
    buzzer.on()
    sleep(5)
    buzzer.off()

def motor_and_servo():
    green = LED(16)
    red = LED(20)
    blue = LED(21)

    motorA1pin = 17
    motorA2pin = 27
    motorAenablePin = 22

    motorB1pin = 24
    motorB2pin = 23
    motorBenablePin = 25

    arm = 13
    grab = 19
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(arm, GPIO.OUT)
    GPIO.setup(grab, GPIO.OUT)

    s1 = GPIO.PWM(arm, 50)  # GPIO 17 for PWM with 50Hz
    s2 = GPIO.PWM(grab, 50)  # GPIO 17 for PWM with 50Hz

    s1.start(6)  # Initialization
    s2.start(3)

    temp1 = 1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motorA1pin, GPIO.OUT)
    GPIO.setup(motorA2pin, GPIO.OUT)
    GPIO.setup(motorAenablePin, GPIO.OUT)
    GPIO.output(motorA1pin, GPIO.LOW)
    GPIO.output(motorA2pin, GPIO.LOW)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motorB1pin, GPIO.OUT)
    GPIO.setup(motorB2pin, GPIO.OUT)
    GPIO.setup(motorBenablePin, GPIO.OUT)
    GPIO.output(motorB1pin, GPIO.LOW)
    GPIO.output(motorB2pin, GPIO.LOW)

    mA = GPIO.PWM(motorAenablePin, 750)
    mB = GPIO.PWM(motorBenablePin, 750)
    mA.start(75)
    mB.start(75)

    x = 48
    y = True


    while (1):
        if (ser.in_waiting > 0):
            read_val = ser.read()
            x = ord(read_val)

        if x == 98:
            ringBuzzer()
            break

        if x == 116:  # t
            y = True
        if y == False:
            if x == 55:  # 7
                s1.ChangeDutyCycle(4.5)
                sleep(1)
                s2.ChangeDutyCycle(5)
            elif x == 56:  # 8
                s1.ChangeDutyCycle(6)
                # s2.ChangeDutyCycle(k)
            elif x == 57:  # 9
                s1.ChangeDutyCycle(4.5)
                s2.ChangeDutyCycle(3)
            elif x == 114:  # red LED
                red.on()
            elif x == 103:  # green led
                green.on()
            elif x == 98:  # blue led
                blue.on()
            elif x == 121:  # yellow led
                red.on()
                green.on()
        if y:
            if x == 48:  # 0
                print("stop")
                GPIO.output(motorA1pin, GPIO.LOW)
                GPIO.output(motorA2pin, GPIO.LOW)
                GPIO.output(motorB1pin, GPIO.LOW)
                GPIO.output(motorB2pin, GPIO.LOW)
                x = 122
                y = False

            elif x == 49:  # 1
                print("forward")
                GPIO.output(motorA1pin, GPIO.HIGH)
                GPIO.output(motorA2pin, GPIO.LOW)
                GPIO.output(motorB1pin, GPIO.HIGH)
                GPIO.output(motorB2pin, GPIO.LOW)
                temp1 = 1
                x = 122
            elif x == 50:  # 2
                print("right")
                GPIO.output(motorA1pin, GPIO.LOW)
                GPIO.output(motorA2pin, GPIO.HIGH)
                GPIO.output(motorB1pin, GPIO.HIGH)
                GPIO.output(motorB2pin, GPIO.LOW)
                temp1 = 1
                x = 122
            elif x == 51:  # 3
                print("left")
                GPIO.output(motorA1pin, GPIO.HIGH)
                GPIO.output(motorA2pin, GPIO.LOW)
                GPIO.output(motorB1pin, GPIO.LOW)
                GPIO.output(motorB2pin, GPIO.HIGH)
                temp1 = 1
                x = 122

            elif x == 52:  # 4
                print("backward")
                GPIO.output(motorA1pin, GPIO.LOW)
                GPIO.output(motorA2pin, GPIO.HIGH)
                GPIO.output(motorB1pin, GPIO.LOW)
                GPIO.output(motorB2pin, GPIO.HIGH)
                temp1 = 0
                x = 'z'


        # elif x == 108:
        #   print("low")
        #  mA.ChangeDutyCycle(25)
        # x = 122

        elif x == 113:  # q

            s1.stop()
            s2.stop()
            GPIO.cleanup()
            break

'''
functions in this file:
* angle_calculate(pt1,pt2, trigger = 0) - function to return angle between two points
* detect_Aruco(img) - returns the detected aruco list dictionary with id: corners
* mark_Aruco(img, aruco_list) - function to mark the centre and display the id
* calculate_Robot_State(img,aruco_list) - gives the state of the bot (centre(x), centre(y), angle)
'''


def angle_calculate(pt1, pt2, trigger=0):  # function which returns angle between two points in the range of 0-359
    angle_list_1 = list(range(359, 0, -1))
    # angle_list_1 = angle_list_1[90:] + angle_list_1[:90]
    angle_list_2 = list(range(359, 0, -1))
    angle_list_2 = angle_list_2[-90:] + angle_list_2[:-90]
    x = pt2[0] - pt1[0]  # unpacking tuple
    y = pt2[1] - pt1[1]
    angle = int(math.degrees(
        math.atan2(y, x)))  # takes 2 points nad give angle with respect to horizontal axis in range(-180,180)
    if trigger == 0:
        angle = angle_list_2[angle]
    else:
        angle = angle_list_1[angle]
    return int(angle)


def detect_Aruco(img):  # returns the detected aruco list dictionary with id: corners
    aruco_list = {}
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.getPredefinedDictionary(
        aruco.DICT_7X7_1000)  # aruco.Dictionary_get(aruco.DICT_4X4_50)   #creating aruco_dict with 5x5 bits with max 250 ids..so ids ranges from 0-249
    #print(aruco_dict)
    parameters = aruco.DetectorParameters_create()  # refer opencv page for clarification
    # lists of ids and the corners beloning to each id
    #print(parameters)
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    # corners is the list of corners(numpy array) of the detected markers. For each marker, its four corners are returned in their original order (which is clockwise starting with top left). So, the first corner is the top left corner, followed by the top right, bottom right and bottom left.
    # print len(corners), corners, ids
    #print(corners)

    gray = aruco.drawDetectedMarkers(gray, corners, ids)
    # cv2.imshow('frame',gray)
    # print (type(corners[0]))
    if len(corners):  # returns no of arucos

        for k in range(len(corners)):
            temp_1 = corners[k]
            temp_1 = temp_1[0]
            temp_2 = ids[k]
            temp_2 = temp_2[0]
            aruco_list[temp_2] = temp_1
        #print('Aruco List:',aruco_list)
        return aruco_list


def mark_Aruco(img, aruco_list):  # function to mark the centre and display the id
    key_list = aruco_list.keys()
    font = cv2.FONT_HERSHEY_SIMPLEX
    for key in key_list:
        dict_entry = aruco_list[key]  # dict_entry is a numpy array with shape (4,2)
        centre = dict_entry[0] + dict_entry[1] + dict_entry[2] + dict_entry[
            3]  # so being numpy array, addition is not list addition
        centre[:] = [int(x / 4) for x in centre]  # finding the centre
        # print centre
        orient_centre = centre + [0.0, 5.0]
        # print orient_centre
        centre = tuple(centre)
        orient_centre = tuple((dict_entry[0] + dict_entry[1]) / 2)
        # print centre
        # print orient_centre
        '''
        cv2.circle(img, centre, 1, (0, 0, 255), 8)
        cv2.circle(img, tuple(dict_entry[0]), 1, (0, 0, 255), 8)
        cv2.circle(img, tuple(dict_entry[1]), 1, (0, 255, 0), 8)
        cv2.circle(img, tuple(dict_entry[2]), 1, (255, 0, 0), 8)
        cv2.circle(img, orient_centre, 1, (0, 0, 255), 8)
        '''
        #cv2.line(img, centre, orient_centre, (255, 0, 0), 4)  # marking the centre of aruco
        #cv2.putText(img, str(key), (int(centre[0] + 20), int(centre[1])), font, 1, (0, 0, 255), 2,cv2.LINE_AA)  # displaying the idno
    return img


def calculate_Robot_State(img, aruco_list):  # gives the state of the bot (centre(x), centre(y), angle)
    robot_state = {}
    key_list = aruco_list.keys()
    font = cv2.FONT_HERSHEY_SIMPLEX

    for key in key_list:
        dict_entry = aruco_list[key]
        pt1, pt2 = tuple(dict_entry[0]), tuple(dict_entry[1])
        centre = dict_entry[0] + dict_entry[1] + dict_entry[2] + dict_entry[3]
        centre[:] = [int(x / 4) for x in centre]
        centre = tuple(centre)
        # print centre
        angle = angle_calculate(pt1, pt2)
        #cv2.putText(img, str(angle), (int(centre[0] - 80), int(centre[1])), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        robot_state[key] = (int(centre[0]), int(centre[1]),angle)  # HOWEVER IF YOU ARE SCALING IMAGE AND ALL...THEN BETTER INVERT X AND Y...COZ THEN ONLY THE RATIO BECOMES SAME
    #print(robot_state)

    return robot_state
def colorDetect(frame):
    lower = {'red': (166, 84, 141), 'green': (66, 122, 129), 'blue': (97, 100, 117),
             'yellow': (23, 59, 119)}  # assign new item lower['blue'] = (93, 10, 0)
    upper = {'red': (186, 255, 255), 'green': (86, 255, 255), 'blue': (117, 255, 255), 'yellow': (54, 255, 255)}

    # define standard colors for circle around the object
    colors = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0), 'yellow': (0, 255, 217)}
    while True:
        # grab the current frame

        frame = imutils.resize(frame, width=600)

        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # for each color in dictionary check object in frame
        for key, value in upper.items():
            # construct a mask for the color from dictionary`1, then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            kernel = np.ones((9, 9), np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                x = int(x)
                y = int(y)
                radius = int(radius)
                print([x, y], radius,key)
                M = cv2.moments(c)
                # center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # only proceed if the radius meets a minimum size. Correct this value for your obect's size
                if radius > 50.0:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (x, y), radius, colors[key], 2)

        # show the frame to our screen
        return frame


