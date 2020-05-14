'''
Before launching make sure that:
1) The necessary libraries are installed
2) In the folder with the program there is a necessary image named "test_image" and a white canvas 4000x4000 px named "test" 
'''

import cv2
import math
import random
import numpy as np
from datetime import datetime
import time

start_time = datetime.now() #start of the time counter

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image=cv2.imread("test.jpg")#loading the canvas 4000 by 4000
image2=cv2.imread("test_image.jpg")#uploading the original

image2 = cv2.resize(image2, None, fx = 4, fy = 4, interpolation = cv2.INTER_CUBIC)#We increase the size of the original 4 times

width_copy=image2.shape[0]#photo width
height_copy=image2.shape[1]#photo height

radius=10
x1=2000
y1=2000
procent=0
x=2000
y=2000
spiral=32
#draw a spiral
for i in range(0,360*150):
	radius+=20/360#increase the radius per one turnover by 20 px
	print(toFixed(i/(360*150)*100,2),"%",sep='',end='')#printing percentages to the console
	print('\r', end='')
	try:#taking the average RGB value
		B=image2.item(int(width_copy//2)-int(math.cos(math.radians(i))*radius), int(height_copy//2)+int(math.sin(math.radians(i))*radius),0)
		G=image2.item(int(width_copy//2)-int(math.cos(math.radians(i))*radius), int(height_copy//2)+int(math.sin(math.radians(i))*radius),1)
		R=image2.item(int(width_copy//2)-int(math.cos(math.radians(i))*radius), int(height_copy//2)+int(math.sin(math.radians(i))*radius),2)
		S=(B+G+R)//3
	except IndexError :
		S=0
	if S<=5:
		spiral_distance=1
	else:
		spiral_distance=int((spiral/2)*( (255-S) / 255 ) + 1 )#defining the line thickness at a certain moment
	cv2.line(image, (x1, y1), (x+int(math.cos(math.radians(i))*radius), y+int(math.sin(math.radians(i))*radius)), (0, 0, 0), spiral_distance)#each degree of the spiral = one line.
	x1=x+int(math.cos(math.radians(i) )*radius)
	y1=y+int(math.sin(math.radians(i))*radius)

#turning the image on 90 degrees
(h, w, d) = image.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
image = cv2.warpAffine(image, M, (w, h))

cv2.imwrite("result.jpg", image)#Saving the result
print('Done!')
print(datetime.now() - start_time)#end of the time counter
viewImage(image, "test")