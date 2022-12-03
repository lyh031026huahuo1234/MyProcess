import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../wk.jpg',0)
equ = cv.equalizeHist(img)  #得到直方图均衡图像
res = np.hstack((img,equ))  #将像素横向堆叠
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv.imshow('res',res)
cv.imshow('cl1',cl1)
cv.waitKey(0)
cv.destroyAllWindows()