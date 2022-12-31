
import cv2 as cv

# 1.读入图像
import matplotlib.pyplot as plt

img=cv.imread('1.jpg')

# 2.图像缩放
# 2.1 绝对尺寸缩放
rows,cols = img.shape[:2]
res = cv.resize(img,(5*cols,5*rows),interpolation=cv.INTER_CUBIC)

# 2.2 相对尺寸缩放
res1 = cv.resize(img,None,fx=0.5,fy=0.5)

#图像显示
fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(10,8),dpi=100)
axes[0].imshow(res[:,:,::-1])
axes[0].set_title('absolute_scale')
axes[1].imshow(img[:,:,::-1])
axes[2].imshow(res1[:,:,::-1])
axes[2].set_title('relative scale')
plt.show()


