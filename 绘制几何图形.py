import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1.创建一个全黑的空白图像
img = np.zeros((512,512,3),np.uint8)

# 2.绘制图形
# 起点坐标为左上角，终点坐标为右下角，颜色为蓝色（BGR存储顺序），宽度设为5
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
# 圆心位置，半径，颜色，宽度
cv.circle(img,(447,63),63,(0,0,255),-1)
# 指定文字字体
font = cv.FONT_HERSHEY_SIMPLEX
# 指定文字的位置，字体，大小，颜色，线条宽度，线性展示
cv.putText(img,'OpenCv',(10,500),font,4,(255,255,255),2,cv.LINE_AA)

# 3.图像显示
plt.imshow(img[:,:,::-1])
plt.title('matplotlib')
plt.show()