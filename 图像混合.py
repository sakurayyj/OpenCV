import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

# 1.读入图像
img1=cv.imread('2.jpg')
img2=cv.imread('3.jpg')

# 2.图像加法
img3 = cv.addWeighted(img1,0.7,img2,0.3,255) # cv中加法

# 3.图像显示
plt.figure(figsize=(8,8))
plt.imshow(img3[:,:,::-1])
plt.show()
