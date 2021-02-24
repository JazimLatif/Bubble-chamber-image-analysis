from __future__ import division 
import cv2
import numpy as np

# importing the image
img = cv2.imread(r'C:\Users\jclat\OneDrive\Desktop\353\sudoku.jpg')
# making the image greyscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# applying canny edge detection to the image
edges = cv2.Canny(gray,5,15,apertureSize = 3)

# applying the probabilistic Hough transformation
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, minLineLength=100, maxLineGap=2)

test1 = [[3,6],[52,51]]
test2 = [[1,4],[2,6]]

# calculating gradient of the first tangent line
dx_1 = test1[0][0] - test1[1][0] #lines[1][0][0] - lines[1][0][2]
dy_1 = test1[0][1] - test1[1][1] #lines[1][0][1] - lines[1][0][3]
grad_1 = dy_1 / dx_1
tang_grad_1 = -1 / grad_1

# midpoint of first line
x_mid_1 = (test1[0][0] + test1[1][0])/2 #lines[1][0][0] - lines[1][0][2]
y_mid_1 = (test1[0][1] + test1[1][1])/2 #lines[1][0][1] - lines[1][0][3]

# constructing first tangent line
a = tang_grad_1
c = -tang_grad_1 * x_mid_1 + y_mid_1

# calculating gradient of the second tangent line
dx_2 = test2[0][0] - test2[1][0] #lines[2][0][0] - lines[2][0][2]
dy_2 = test2[0][1] - test2[1][1] #lines[2][0][1] - lines[2][0][3]
grad_2 = dy_2 / dx_2
tang_grad_2 = -1 / grad_2

# midpoint of second line
x_mid_2 = (test2[0][0] + test2[1][0])/2 #lines[2][0][0] - lines[2][0][2]
y_mid_2 = (test2[0][1] + test2[1][1])/2 #lines[2][0][1] - lines[2][0][3]

# constructing second tangent line
b = tang_grad_2
d = -tang_grad_2 * x_mid_2 + y_mid_2

# calculating intersection
p_x = (d-c)/(a-b)
p_y = a * p_x + c

print([p_x,p_y])

