"""
I used code from these two sources:
Video Capture: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
Feature: https://github.com/opencv/opencv/blob/master/samples/python/edge.py

Modification done:
I covered all non-edges with pink, leaving only detected edges visible in the camera feed

"""

import numpy as np
import cv2 as cv

#~~~~~~~~~~~~~~~ Capture video ~~~~~~~~~~~~~~~~~~~
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # ADDITIONAL FEATURE:
    thrs1 = cv.getTrackbarPos('thrs1', 'edge')
    thrs2 = cv.getTrackbarPos('thrs2', 'edge')
    edge = cv.Canny(gray, thrs1, thrs2, apertureSize=5)
    vis = frame.copy()
    vis = np.uint8(vis/2.)
    #vis[edge != 0] = (0, 255, 0) #original line of code 

    #PERSONALISED MODIFICATION:
    vis[edge == 0] = (147, 112, 219)
    
    

    # Display the resulting frame
    cv.imshow('edge', vis)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

#~~~~~~~~~~~~~~~~ Save video ~~~~~~~~~~~~~~~~~~

