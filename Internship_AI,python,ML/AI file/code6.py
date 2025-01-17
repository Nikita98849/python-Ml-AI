import cv2  
import numpy as np  
   
# path to input image is specified and   
# image is loaded with imread command  
image = cv2.imread('lamp.png')  
   
 
# to convert the image in grayscale  
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
ret, th1 = cv2.threshold(img,160, 255, cv2.THRESH_BINARY) 
   
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,11,2)
 
cv2.imshow('Original',image)
cv2.imshow('Binary Threshold', th1) 
cv2.imshow('Adaptive Threshold', th2) 
cv2.imshow('Gaussain Adaptive Threshold', th3) 
     
# De-allocate any associated memory usage   
cv2.waitKey(0)
cv2.destroyAllWindows() 
