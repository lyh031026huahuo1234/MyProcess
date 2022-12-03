import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
    global drawing,ix,iy
    if event == cv.EVENT_FLAG_LBUTTON:
        drawing = True
        ix,iy = x,y
    if event == cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        if drawing == True:
            #cv.rectangle(img,(ix,iy),(x,y),(250,123,123),-1)
            cv.line(img,(ix,iy),(x,iy),(133,133,133),2)
            cv.line(img,(x,iy),(x,y),(133,133,133),2)
            cv.line(img,(x,y),(ix,y),(133,133,133),2)
            cv.line(img,(ix,y),(ix,iy),(133,133,133),2)
            drawing = False
        elif event == cv.EVENT_FLAG_LBUTTON:
            drawing = False
            
            
            
# 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()