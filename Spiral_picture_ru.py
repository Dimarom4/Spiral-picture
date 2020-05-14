'''
Перед запуском убедитесь что:
1)Установлены нужные библиотеки
2)В папке с программой есть нужное изображение с именем test_image и белое полотно 4000х4000 px.
'''

import cv2
import math
import random
import numpy as np
from datetime import datetime
import time

start_time = datetime.now() #Начало счетчика времени

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def viewImage(image, name_of_window):#просмотр изображения
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image=cv2.imread("test.jpg")#Загружаем полотно 4000 на 4000
image2=cv2.imread("test_image.jpg")#Загружаем оригинал

image2 = cv2.resize(image2, None, fx = 4, fy = 4, interpolation = cv2.INTER_CUBIC)#Увеличиваем размер оригинала в 4 раза

width_copy=image2.shape[0]#ширина оригинала
height_copy=image2.shape[1]#высота копии

radius=10
x1=2000
y1=2000
procent=0
x=2000
y=2000
spiral=32
#рисуем спираль
for i in range(0,360*150):
	radius+=20/360#увеличение радиуса за один оборот на 20 px
	print(toFixed(i/(360*150)*100,2),"%",sep='',end='')#печать процентов в консоль
	print('\r', end='')
	try:#Берем среднее значение RGB
		B=image2.item(int(width_copy//2)-int(math.cos(math.radians(i))*radius), int(height_copy//2)+int(math.sin(math.radians(i))*radius),0)
		G=image2.item(int(width_copy//2)-int(math.cos(math.radians(i))*radius), int(height_copy//2)+int(math.sin(math.radians(i))*radius),1)
		R=image2.item(int(width_copy//2)-int(math.cos(math.radians(i))*radius), int(height_copy//2)+int(math.sin(math.radians(i))*radius),2)
		S=(B+G+R)//3
	except IndexError :
		S=0
	if S<=5:
		spiral_distance=1
	else:
		spiral_distance=int((spiral/2)*( (255-S) / 255 ) + 1 )#определяем толщину линии в определенный момент
	cv2.line(image, (x1, y1), (x+int(math.cos(math.radians(i))*radius), y+int(math.sin(math.radians(i))*radius)), (0, 0, 0), spiral_distance)#Каждый градус спирали = одна линия.
	x1=x+int(math.cos(math.radians(i) )*radius)
	y1=y+int(math.sin(math.radians(i))*radius)

#поворот изображения на 90 градусов
(h, w, d) = image.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
image = cv2.warpAffine(image, M, (w, h))

cv2.imwrite("result.jpg", image)#Сохранение результата
print('Done!')
print(datetime.now() - start_time)#Конец счетчика времени
viewImage(image, "test")#Просмотр изображения