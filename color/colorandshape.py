from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np


def detect_contour(path):
    frame = cv2.imread(path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    th = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)[1]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    inputDict = {'blue': 'square', 'green': 'circle'}
    lower = {'red': (-10, 245, 214), 'green': (41, 245, 143), 'blue': (99, 158, 159)}
    upper = {'red': (10, 265, 294), 'green': (86, 255, 255), 'blue': (119, 178, 239)}
    boundaryColor = None

    for key, values in upper.items():
        color = key
        if color in inputDict.keys():
            kernel = np.ones((9, 9), np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            if color == 'red':
                boundaryColor = (0, 255, 0)
            elif color == 'green':
                boundaryColor = (255, 0, 0)
            elif color == 'blue':
                boundaryColor = (0, 0, 255)
            ctr = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)[-2]
            for i in ctr:

                '''shape detection begins...'''
                shape = 'unidentified'
                p = cv2.arcLength(i, True)  # perimeter
                approx = cv2.approxPolyDP(i, 0.04 * p, True)

                if len(approx) == 3:
                    shape = "triangle"
                elif len(approx) == 4:
                    (x, y, w, h) = cv2.boundingRect(approx)
                    ar = w / float(h)

                    # a square will have an aspect ratio that is approximately
                    # equal to one, otherwise, the shape is a rectangle
                    shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
                else:
                    shape = 'circle'
                '''shape ends...'''
                if shape == inputDict[key]:
                    # coord and outline
                    M = cv2.moments(i)
                    ix = int(M["m10"] / M["m00"])
                    iy = int(M["m01"] / M["m00"])
                    print([ix, iy])
                    cv2.drawContours(frame, [i], -1, boundaryColor, 25)

                    cv2.circle(frame, (ix, iy), 3, (0, 0, 0), -1)
                    text = '(' + str(ix) + ',' + str(iy) + ')'
                    print(text)
                    cv2.putText(frame, text, (ix - 20, iy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

            cv2.imshow('image', mask)
            cv2.waitKey(0)

        # draw the contour and center of the shape on the image

    cv2.imshow("Image", frame)
    cv2.waitKey(0)
path_to_image = 'img1.jpg'
if __name__=='__main__':
    detect_contour(path_to_image)