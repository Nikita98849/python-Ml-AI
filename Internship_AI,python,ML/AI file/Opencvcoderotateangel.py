import cv2
import numpy as np
 
#importing the opencv module  
import cv2  
# using imread('path') and 1 denotes read as  color image  
img = cv2.imread(r'flower1.jpg',1)  
# get image height, width
(h, w) = img.shape[:2]
# calculate the center of the image
center = (w / 2, h / 2)
  
scale = 1.0
  
# Perform the counter clockwise rotation holding at the center
# 45 degrees
M = cv2.getRotationMatrix2D(center, 45, scale)
print(M)
rotated45 = cv2.warpAffine(img, M, (h, w))
  
# 110 degrees
M = cv2.getRotationMatrix2D(center,110, scale)
rotated110 = cv2.warpAffine(img, M, (w, h))
  
# 150 degrees
M = cv2.getRotationMatrix2D(center, 150, scale)
rotated150 = cv2.warpAffine(img, M, (h, w))
  
  
cv2.imshow('Original Image',img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
  
cv2.imshow('Image rotated by 45 degrees',rotated45)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
  
cv2.imshow('Image rotated by 110 degrees',rotated110)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
  
cv2.imshow('Image rotated by 150 degrees',rotated150)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
