#importing the opencv module  
import cv2  
# using imread('path') and 1 denotes read as  color image  
img = cv2.imread(r'C:\Users\Vineet\Downloads\dog.jpg',1)  
#This is using for display the image  
cv2.imshow('image',img)  
cv2.waitKey() # This is necessary to be required so that the image doesn't close immediately.  
#It will run continuously until the key press.  
cv2.destroyAllWindows() 
