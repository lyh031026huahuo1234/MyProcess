import numpy as np
import cv2 as cv

img1 = cv.imread('../kodim01.png')
img2 = cv.imread('../kodim23.png')
dst = cv.addWeighted(img1,0.5,img2,0.5,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()