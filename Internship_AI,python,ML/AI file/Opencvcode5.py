import cv2  
import numpy as np  
   
# path to input image is specified and   
# image is loaded with imread command  
image = cv2.imread('dog.jpg')  
   
 
# to convert the image in grayscale  
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
   
threshold=160
ret, thresh1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY) 
ret, thresh2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV) 
ret, thresh3 = cv2.threshold(img, threshold, 255, cv2.THRESH_TRUNC) 
ret, thresh4 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO) 
ret, thresh5 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV) 
   
# the window showing output images 
# with the corresponding thresholding  
# techniques applied to the input images 
cv2.imshow('Original',image)
cv2.imshow('Binary Threshold', thresh1) 
cv2.imshow('Binary Threshold Inverted', thresh2) 
cv2.imshow('Truncated Threshold', thresh3) 
cv2.imshow('Zero Threshold', thresh4) 
cv2.imshow('Zero Inverted', thresh5) 
     
# De-allocate any associated memory usage   
cv2.waitKey(0)
cv2.destroyAllWindows() 
