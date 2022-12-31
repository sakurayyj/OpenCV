import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt#1读取图像
img1 = cv.imread("img_1.png")
img2 = cv.imread( "img_2.png")
# 2创建核结构
kernel = np.ones( (10,10),np.uint8)#3图像的开闭运算
cv0pen = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)
#开运算
cvClose = cv.morphologyEx(img2, cv.MORPH_CLOSE,kernel)#闭运算#4图像展示+
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,8))
axes [0,0].imshow(img1)
axes [0,0].set_title("before")
axes [0,1] .imshow( cv0pen)
axes[0,1].set_title("open")
axes[1,0].imshow(img2)
axes[1,0].set_title("before")
axes[1,1].imshow(cvClose)
axes[1,1].set_title("close")
plt.show()
