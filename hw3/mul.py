import numpy as np
import cv2 as cv

def multiply_demo(img, num):
    dst = cv.multiply(img,(num,num,num,num))
    return dst


if __name__ == '__main__':
    img = cv.imread('../kodim01.png')
    num = float(input())
    dst = multiply_demo(img,num)
    #dst = cv.imread('../kodim23.png')
    # cv.imshow('img',img)
    # cv.imshow('dst',dst)
    for alp in range(0,100,1):
        now = cv.addWeighted(img,1-float(alp/100),dst,float(alp/100),0)
        cv.imshow('now',now)
        cv.waitKey(60)
    cv.waitKey(0)
    cv.destroyAllWindows()