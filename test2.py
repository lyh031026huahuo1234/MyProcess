import numpy as np
import cv2 as cv
# 创建黑色的图像
img = np.zeros((512,512,3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
cv.rectangle(img,(0,0),(510,510),(0,0,255),3)
cv.imshow("shape",img)
cv.waitKey(0)
cv.destroyAllWindows()