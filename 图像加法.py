import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

# 1.读入图像
img1=cv.imread('2.jpg')
img2=cv.imread('3.jpg')

# 2.图像加法
img3 = cv.add(img1,img2) # cv中加法
img4 = img1+img2 # 直接相加

# 3.图像显示
fig,axes = plt.subplots(nrows=1,ncols=2,figsize = (10,8),dpi = 100)
axes[0].imshow(img3[:,:,::-1])
axes[0].set_title('cv')
axes[1].imshow(img4[:,:,::-1])
axes[1].set_title('numpy')
plt.show()