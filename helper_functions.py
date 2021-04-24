#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Range detector to find out color ranges for particular object in the video or image 

import cv2
from operator import xor

def callback(value):
    pass

def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)
    # Create trackbars
    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)

def get_trackbar_values(range_filter):
    values = []
    # Get trackbaer position and return values
    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)

    return values

def color_range_detector(filt,path):
    
    range_filter = filt.upper()
    
    # Read image and resize 
    img = cv2.imread(path)
    img = cv2.resize(img,(350,350))
    
    # Convert to HSV color space
    if range_filter == 'RGB':
        frame_to_thresh = img.copy()
    else:
        frame_to_thresh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
    setup_trackbars(range_filter)

    while True:
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)
        # Get current threshold values
        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))
        cv2.imshow("Original", img)
        cv2.imshow("Thresh", thresh)
        
        # Press 'e' to end the color range detector
        if cv2.waitKey(1) & 0xFF is ord('e'):
            break


# In[1]:


#path = 'Range.jpg'
#path = 'ball_track.jpg'
#filt = 'rgb'
#color_range_detector(filt,path)

