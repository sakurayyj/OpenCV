import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
img = cv.imread('4.jpg')
plt.imshow(img[:,:,::-1])
plt.show()
# 获取某个像素点的值
px = img[100,100]
# 仅获取蓝色通道的强度值
blue = img[100,100,0]
# 修改某个位置的像素值
img[100,100] = [0,0,255]
plt.imshow(img[:,:,::-1])
plt.show()