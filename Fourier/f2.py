import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../kodim23.png',0)
rows = img.shape[0]
cols = img.shape[1]
crow,ccol = rows//2, cols//2
f = np.fft.fft2(img)
#进行位置的调整
fshift = np.fft.fftshift(f)
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
mask = np.zeros((rows,cols,2), np.uint8)
mask[crow-300:crow+300, ccol-300:ccol+300] = 1
# print(crow)
# print(ccol)
#fshift[crow-30:crow+30, ccol-30:ccol+31] = 0    #去除低频的信号
# print(fshift.shape)
# print(mask.shape)
# fshift = fshift*mask[:,:,-1]
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
# img_back = np.fft.ifft2(f_ishift)   #逆傅里叶变换还原图像
# img_back = np.real(img_back)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])
cv.imshow('original', img)
cv.imshow('change',img_back)
cv.waitKey(0)
cv.destroyAllWindows()
