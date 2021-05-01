### Object_detection_tracking
  
  #### The given implementation is used to detect any circular (spherical objects in the image with a specific color)
  #### There are two python(.py) files in this project. "object_tracking.py" contains implementation of object tracking in the video and "helper_functions.py" contains required         functions to carry out range detection of the specific object.
  ##### 1.How to use object_tracking model : 
   ###### Input to the object tracking model : "videopath", "blueLower", "blueUpper" and "buffer"
   ###### videopath : path of the video in which specific object is to be detected
   ###### blueLower & blueUpper : lower and upper hsv color space range of the object to be detected in the image
   ###### buffer : buffer is the minimum number of previously tracked points in the vides
   ###### If you are not able to detect any object, please tune the upper and lower ranges
  ##### 2.How to use range_detection function : 
   ###### Input to the range detection function : "filter" and "template_path"
   ###### filter : 'rgb' or 'hsv' color space can be used
   ###### template_path : image path of the object for which color range is to be detected
   ###### run the range_detection function and find out the lower & upper range of the circular (spherical object) you want to detect
  ##### 3.To detect object with thick continuos boundaries : 
   ###### Morphology functions in cv2 can be used for detection of the object with thick continuos boundaries
   ###### The required functions are already implemented. Please check commented lines 46-50
