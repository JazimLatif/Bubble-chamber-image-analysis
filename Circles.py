import cv2
import numpy as np
import scipy 

img = cv2.imread(r'C:\Users\jclat\OneDrive\Desktop\353\ring.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    #draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)


cv2.imwrite(r'C:\Users\jclat\OneDrive\Desktop\353\output_ring.jpg',img)
