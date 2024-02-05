from circleDetection import *
import numpy as np
import cv2 as cv

def videoStreamProcess(port):
    #open video
    capture = cv.VideoCapture(port)

    while True:
        #capture frame
        ret, frame = capture.read()

        #if frame is read correctly ret is True

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # process frame
        procFrame = circleDetection(frame)
        # Display the resulting frame
        cv.imshow('frame', procFrame)
        if cv.waitKey(1) == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()