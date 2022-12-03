import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
"""获取二维直方图"""
img = cv.imread('../kodim01.png')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

plt.imshow(hist,interpolation = 'nearest')
plt.show()