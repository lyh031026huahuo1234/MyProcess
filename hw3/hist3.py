import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../kodim01.png',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()     #获取累计和
cdf_normalized = cdf * float(hist.max()) / cdf.max()
cdf_m = np.ma.masked_equal(cdf,0)   #创建掩码
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
#plt.plot(cdf, color = 'b')
# #plt.plot(cdf, color = 'g')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.hist(img2.flatten(),256,[0,256], color = 'g')
plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
cv.imshow('img',img)
cv.imshow('img2',img2)
cv.waitKey(0)
cv.destroyAllWindows()