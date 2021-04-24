# Circular object detection (To be specific spherical objects.viz, ball, spherical fruits)
# Use helping range_detect.ipynb to get the color range for the specific object (color) 
# To detect object with thick continuos boundaries use Morphology functions in cv2 (uncomment the required lines 46-50)

from collections import deque
from imutils.video import VideoStream
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
from helper_functions import *
get_ipython().run_line_magic('matplotlib', 'inline')

def Ball_Detection(videopath,blueLower,blueUpper,buffer=64):
    # List of tracked points
    PointList = deque(maxlen=buffer)
        
    # Reference to the video file
    vr = cv2.VideoCapture(videopath)

    while True:
        # Capture video frame
        frame = vr.read()
        frame = frame[1]
        
        # End of the video
        if frame is None:
            break
            
        # Resize the frame
        frame   = imutils.resize(frame, width=1000)
        # Blurr the frame
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        # Convert the frame from BGR to HSV space , cv2 reads the image in default BGR 
        hsv     = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        # Create mask for blue color and Image morphology
        # HSV color range for blue color defined by blueLower and blueUpper 
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        # Erode the mask to remove noise in the mask
        mask = cv2.erode(mask, None, iterations=2)
        # Dilate the image to enhance the boundaries in the mask
        mask = cv2.dilate(mask, None, iterations=2)
        
        # Alternatively morphologyEx can be used, eroding followed by dilating
        # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, iterations=2)
        
        # For hollow circular bodies or objects use 
        # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, iterations=2)
     
        # Initialize the contours and center of the circle (x, y)
        cnts   = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts   = imutils.grab_contours(cnts)
        center = None
        
        if len(cnts) > 0:
            # Find largest contour in the mask and use to compute the minimum enclosing circle center
            c = max(cnts, key = cv2.contourArea)
            ((x, y), rad) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
            # if radius goes above certain value
            if rad > 10:
                # Drawing circle and center
                cv2.circle(frame, (int(x), int(y)), int(rad), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 255, 0), -1)
                
        # Append in the points list
        PointList.appendleft(center)
        
        # Loop over the set of tracked points
        for i in range(1, len(PointList)):
            # If no points tracked ignore them
            if PointList[i - 1] is None or PointList[i] is None:
                continue
                
            # Compute the thickness of the line and draw connecting lines
            thickness = int(np.sqrt(buffer / float(i + 1)) * 2.5)
            cv2.line(frame, PointList[i - 1], PointList[i], (0, 0, 255), thickness)
            
        # Show the frames to user
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
        # Press 'e' key to stop the loop
        if key == ord("e"):
            break
                
    # close all windows
    cv2.destroyAllWindows()
    
#blueLower= (10, 75, 150)
#blueUpper= (206, 218, 255)
#buffer = 64
#videopath = 'ball_tracking_3.mp4'
#Ball_Detection(videopath,blueLower,blueUpper,buffer)

