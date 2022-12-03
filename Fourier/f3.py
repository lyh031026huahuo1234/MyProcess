import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
"""用opencv来获得傅立叶变换结果"""

img = cv.imread('../wk.jpg',0)
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


rows = img.shape[0]
cols = img.shape[1]
crow, ccol = rows//2, cols//2
"""去除高频信号"""
mask = np.zeros((rows,cols,2), np.uint8)
mask[crow-50:crow+50, ccol-50:ccol+50] = 1

fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0], img_back[:,:,1])   #计算复数的模

cv.imshow('img',img)
cv.imshow('change',img_back)
cv.waitKey(0)
cv.destroyAllWindows()

# cv.imshow('img',img)
# cv.imshow('f',magnitude_spectrum)
# cv.waitKey(0)
# cv.destroyAllWindows()
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()
