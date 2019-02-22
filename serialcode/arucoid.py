from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import csv
import aruco_lib


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

#cap = cv2.VideoCapture(0)



def get_aruco_list():
    ids = []  # list to store Aruco IDs Scanned

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        if len(ids)==4:
            return ids
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        det_aruco_list = aruco_lib.detect_Aruco(image)
        if det_aruco_list:
            #print('Arduco detected')
            #image = aruco_lib.mark_Aruco(frame, det_aruco_list)
            robot_state = aruco_lib.calculate_Robot_State(image, det_aruco_list)
            id_raw = robot_state.keys()
            for i in id_raw:
                if i not in ids:
                    ids.append(i)
                    print('ID Detected:',i)
        #cv2.imshow("Frame", image)
        #key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        #if key == ord("q"):
            #cv2.destroyAllWindows()
            #print(ids)
            #break
def getColorlist():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        frame = aruco_lib.colorDetect(image)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        if key == ord("q"):
            cv2.destroyAllWindows()
            break