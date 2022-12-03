import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../kodim23.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
cv.imshow('hist',img)
cv.waitKey(0)
cv.destroyAllWindows()