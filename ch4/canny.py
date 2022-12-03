import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../kodim01.png',0) #灰度图
edges = cv.Canny(img,100,200)   #边界图
cv.imshow('img',img)
cv.imshow('edge',edges)
cv.waitKey(0)
cv.destroyAllWindows()
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()