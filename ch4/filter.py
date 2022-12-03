import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def noise(img):
    """椒盐噪声"""
    s_vs_p = 0.5
    amount = 0.04
    noise = np.copy(img)
    #得到噪点的数目
    num_salt = np.ceil(img.size*amount*s_vs_p)
    coords = [np.random.randint(0,i-1, int(num_salt)) for i in img.shape]
    noise[coords[0],coords[1],:] = [255,255,255]
    num_pepper = np.ceil(amount*img.size*(1-s_vs_p))
    coords = [np.random.randint(0,i-1, int(num_pepper)) for i in img.shape]
    noise[coords[0],coords[1],:] = [0,0,0]
    return noise
    


img = cv.imread('../kodim23.png')
noise = noise(img)
kernal = np.ones((5,5),np.float32)/25
dst1 = cv.filter2D(img,-1,kernal)
dst2 = cv.blur(img,(10,10))     #平均
dst3 = cv.GaussianBlur(img,(5,5),0)     #高斯模糊
dst4 = cv.medianBlur(noise,5)     #中位模糊
dst5 = cv.bilateralFilter(img,9,75,75)  #双边滤波
laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
# cv.imshow('img',img)
# cv.imshow('laplaction',laplacian)
# cv.imshow('sobelx',sobelx)
# cv.imshow('sobely',sobely)
# cv.imshow('dst1',dst1)
# cv.imshow('dst2',dst2)
# cv.imshow('dst3',dst3)
cv.imshow('noise',noise)
cv.imshow('dst4',dst4)
#cv.imshow('dst5',dst5)
cv.waitKey(0)
cv.destroyAllWindows()
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()
