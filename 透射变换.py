import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#1读取图像
img = cv.imread("1.jpg")
#2透射变换
rows ,cols = img.shape [ :2]
#2.1创建变换矩阵
pts1 = np.float32( [ [56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32( [ [100,145], [300,100], [80,290],[310,300]])
T= cv.getPerspectiveTransform(pts1,pts2)
#2.2进行变换
dst = cv.warpPerspective( img,T,(cols , rows))
#3图像显示
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes [0] .imshow( img [ : , : , ::-1])
axes [0].set_title("before")
axes[1].imshow(dst[: , : , : :-1])
axes[1].set_title("after")
plt.show( )