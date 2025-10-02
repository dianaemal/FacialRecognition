import numpy as np
import cv2
import os
from mtcnn import MTCNN


# open the default camera
cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# initialize the detector
detector = MTCNN()

if not cam.isOpened():
    print("Error opening the camera.")
    exit()

while True:
    # capture the frames 
    ret, frame = cam.read()

    if not ret:
        print("Can't recieve the frame")
        break

    result = detector.detect_faces(frame)
    x, y, w, h = result[0]["box"]
    # upper left corner of the face:
    ul_corner = (x, y)
    # lower right corner:
    lr_corner = (x+w, y+h)

    # draw a rectangle:
    cv2.rectangle(frame, ul_corner, lr_corner, (0, 255, 0), 2)

    # show the camera feed
    cv2.imshow('Camera Feed', frame)

        # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows
    