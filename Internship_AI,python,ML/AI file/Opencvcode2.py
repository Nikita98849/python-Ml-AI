import cv2
import numpy as np
 
#importing the opencv module  
import cv2  
# using imread('path') and 1 denotes read as  color image  
img = cv2.imread('flower1.jpg',1)  
print(img.shape)
img_resized=cv2.resize(img, (780, 540),  
               interpolation = cv2.INTER_NEAREST) 
cv2.imshow("Resized",img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
