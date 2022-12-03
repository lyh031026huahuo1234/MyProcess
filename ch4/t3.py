import numpy as np
import cv2 as cv
import math
from matplotlib import pyplot as plt



def mov(img,tx,ty):
    rows = img.shape[0]
    cols = img.shape[1]
    M = np.float32([[1,0,tx],[0,1,ty]])
    dst = cv.warpAffine(img,M,(cols,rows))
    return dst

def rigid(img,angle,tx,ty):
    rows = img.shape[0]
    cols = img.shape[1]
    angle = math.radians(angle)
    M = np.float32([[math.cos(angle),-math.sin(angle),tx],[math.sin(angle),math.cos(angle),ty]])
    dst = cv.warpAffine(img,M,(cols,rows))
    return dst

def affine(img):
    rows = img.shape[0]
    cols = img.shape[1]
    ch = img.shape[2]
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    #生成仿射变换的矩阵
    M = cv.getAffineTransform(pts1,pts2)
    dst = cv.warpAffine(img,M,(cols,rows))
    return dst

def similarity(img,s):
    rows = img.shape[0]
    cols = img.shape[1]
    M = np.float32([[s,0,0],[0,s,0]])
    dst = cv.warpAffine(img,M,(cols,rows))
    return dst

def projective(img):
    rows = img.shape[0]
    cols = img.shape[1]
    ch = img.shape[2]
    pts1 = np.float32([[50,50],[370,50],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(cols,rows))
    return dst
    
    

if __name__ == '__main__':
    img = cv.imread("../kodim01.png")
    #tx,ty,angle = map(int,input().split())
    #dst = rigid(img,angle,tx,ty)
    #dst = affine(img)
    # s = float(input())
    # print(s)
    # dst = similarity(img,s)
    # dst = rigid(dst,angle,tx,ty)
    dst = projective(img)
    cv.imshow('img',dst)
    cv.imshow('im',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    