import cv2 as cv
import numpy as np
img = cv.imread('3.png', 0)
cv.imshow("image", img)
k = cv.waitKey(0)&0xFF
if k==27:
    cv.destroyAllWindows()
elif k==ord('s'):
    cv.imwrite('2.png',img)
    cv.destroyAllWindows()
