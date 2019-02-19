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

id_s = []  # list to store SIM ID, Aruco ID pair


if __name__ == '__main__':
    ids = []  # list to store Aruco IDs Scanned

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        det_aruco_list = aruco_lib.detect_Aruco(image)
        if det_aruco_list:
            print('Arduco detected')
            #image = aruco_lib.mark_Aruco(frame, det_aruco_list)
            robot_state = aruco_lib.calculate_Robot_State(image, det_aruco_list)
            id_raw = robot_state.keys()
            for i in id_raw:
                if i not in ids:
                    ids.append(i)
                    ids.sort()
            print(ids)
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            cv2.destroyAllWindows()
            print(ids)
            break

    '''        
    while (True):
        ret, frame = cap.read()
        det_aruco_list = aruco_lib.detect_Aruco(frame)
        if det_aruco_list:
            frame = aruco_lib.mark_Aruco(frame, det_aruco_list)
            robot_state = aruco_lib.calculate_Robot_State(frame, det_aruco_list)
            id_raw = robot_state.keys()
            for i in id_raw:
                if i not in ids:
                    ids.append(i)
                    ids.sort()
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    '''