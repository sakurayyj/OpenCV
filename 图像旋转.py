import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#1读取图像
img = cv.imread("1.jpg")
#2图像旋转
rows ,cols = img.shape[:2]
#2.1 生成旋转矩阵
M= cv.getRotationMatrix2D((cols/2 , rows/2),90,1)
#2.2进行旋转变换
dst = cv .warpAffine( img ,M,(cols , rows ))
#3图像展示
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img[:, : ,::-1])

axes[0].set_title("before")
axes[1].imshow(dst[: ,: , : :-1])
axes[1].set_title("after")
plt.show ( )