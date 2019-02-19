import cv2
import csv
from . import aruco_lib

cap = cv2.VideoCapture(0)

id_s = []  # list to store SIM ID, Aruco ID pair


if __name__ == '__main__':
    ids = []  # list to store Aruco IDs Scanned
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
