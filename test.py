import matplotlib.pyplot as plt
import cv2 as cv

# 读入图像
img=cv.imread('1.jpg',1) # 彩色图形式读取
# img=cv.imread('1.jpg',0) # 灰度图形式读取

# OpenCv显示
cv.imshow('opencv',img)
cv.waitKey(0)

# matplotlib展示
plt.imshow(img[:,:,::-1]) # 彩色图形式显示
#plt.imshow(img,cmap=plt.cm.gray) #灰度图形式显示
plt.title('matplotlib')
plt.show()

# 保存结果
cv.imwrite('11.png',img)