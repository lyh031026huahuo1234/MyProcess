import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../kodim01.png')
kernelx = np.ones((5,1),np.float32)/5
kernely = np.ones((1,5),np.float32)/5

kernelxy = np.ones((5,5),np.float32)/25

dst1 = cv.filter2D(img,-1,kernelx)
dst2 = cv.filter2D(dst1,-1,kernely)
dst3 = cv.filter2D(img,-1,kernelxy)

cv.imshow('img',img)
cv.imshow('dstx',dst1)
cv.imshow('dstx+y',dst2)
cv.imshow('dstxy',dst3)
cv.waitKey(0)
cv.destroyAllWindows()

# plt.subplot(221),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(222),plt.imshow(dst1),plt.title('x')
# plt.xticks([]), plt.yticks([])
# plt.subplot(223),plt.imshow(dst2),plt.title('x+y')
# plt.xticks([]), plt.yticks([])
# plt.subplot(224),plt.imshow(dst3),plt.title('xy')
# plt.xticks([]), plt.yticks([])
# plt.show()