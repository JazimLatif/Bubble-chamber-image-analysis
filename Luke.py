from __future__ import division 
import cv2
import numpy as np
import random

# importing the image
img = cv2.imread(r'C:\Users\jclat\OneDrive\Desktop\353\Circles\3.png')
# making the image greyscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# applying canny edge detection to the image
edges = cv2.Canny(gray,5,15,apertureSize = 3)

# applying the probabilistic Hough transformation
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=20, maxLineGap=2)

# defining empty lists to be used for averages
p_x_list = []
p_y_list = []

# loop over any range
for i in range(100):
    rand_1 = random.randint(1, len(lines))
    rand_2 = random.randint(1, len(lines))

    # calculating gradient of the first tangent line
    dx_1 = lines[rand_1][0][0] - lines[rand_1][0][2]
    dy_1 = lines[rand_1][0][1] - lines[rand_1][0][3]
    grad_1 = dy_1 / dx_1
    tang_grad_1 = -1 / grad_1

    # midpoint of first line
    x_mid_1 = (lines[rand_1][0][0] + lines[rand_1][0][2])/2
    y_mid_1 = (lines[rand_1][0][1] + lines[rand_1][0][3])/2

    # constructing first tangent line
    a = tang_grad_1
    c = -tang_grad_1 * x_mid_1 + y_mid_1

    # calculating gradient of the second tangent line
    dx_2 = lines[rand_2][0][0] - lines[rand_2][0][2]
    dy_2 = lines[rand_2][0][1] - lines[rand_2][0][3]
    grad_2 = dy_2 / dx_2
    tang_grad_2 = -1 / grad_2

    # midpoint of second line
    x_mid_2 = (lines[rand_2][0][0] - lines[rand_2][0][2])/2
    y_mid_2 = (lines[rand_2][0][1] - lines[rand_2][0][3])/2

    # constructing second tangent line
    b = tang_grad_2
    d = -tang_grad_2 * x_mid_2 + y_mid_2

    # calculating intersection
    p_x = (d-c)/(a-b)
    p_y = a * p_x + c

    # appending to empty list
    if np.isnan(p_x) == False:
        p_x_list.append(p_x)
    if np.isnan(p_y) == False:
        p_y_list.append(p_y)

    print([p_x,p_y])
    
# calculating average values
p_x_av = sum(p_x_list) / len(p_x_list)
p_y_av = sum(p_y_list) / len(p_y_list)

# calculating radius of curvature
#R = ((p_x_av - x_mid_1)**2 + (p_y_av - y_mid_1)**2)**0.5

# drawing image at radial centre and exporting
cv2.circle(img, (int(p_x_av),int(p_y_av)), radius=10, color=(0, 0, 255), thickness=-1)

cv2.imwrite(r'C:\Users\jclat\OneDrive\Desktop\353\Circles\output.png',img)
