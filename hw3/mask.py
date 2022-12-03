import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
"""图像掩码的处理"""
img = cv.imread('../kodim23.png',0)
mask = np.zeros(img.shape[:2], np.uint8)
mask[200:500, 200:600] = 255
masked_img = cv.bitwise_and(img,img,mask=mask)

hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()