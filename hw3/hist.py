import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

if __name__ == '__main__':
    img = cv.imread('../kodim01.png',0) #得到灰度图
    # hist = cv.calcHist([img],[0],None,[256],[0,256])   #得到直方图
    # hist,bins = np.histogram(img.ravel(),256,[0,256])   #numpy直方图计算
    plt.hist(img.ravel(),256,[0,256])
    plt.show()
    
    