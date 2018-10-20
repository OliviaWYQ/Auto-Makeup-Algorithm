# -*- coding:utf-8 -*-

from facemask import findpoints, findaffine
import cv2
import time
import numpy as np
import os

LeftPoint = [0, 0]
RightPoint = [0, 0]

def drawPoints(img, pts_2xn, color, radius=1, thickness=-1):
    assert pts_2xn.ndim == 2, 'points_2xn must be 2xn'
    assert pts_2xn.shape[0] == 2, 'points_2xn must be 2xn'
    for idx in range(pts_2xn.shape[1]):
        cv2.circle(img, (int(pts_2xn[0, idx]), int(pts_2xn[1, idx])), radius, color, thickness)
        
def getAffine(filepath1,filepath2,kpath1,kpath2):
    
    frame2 = cv2.imread(filepath2)
    SrcImg = frame2
    
    if SrcImg is not None:
        Img = SrcImg.copy()
    #SrcCanvas = np.zeros(SrcImg.shape, dtype=np.uint8)
    '''
    pointsx1, pointsy1 = findpoints(kpath1)
    pointsx2, pointsy2 = findpoints(kpath2)
    key1 = [[0 for i in range(2)] for i in range(len(pointsx1))]
    key2 = [[0 for i in range(2)] for i in range(len(pointsx2))]
    #key_1 = [(0 for i in range(2)) for i in range(len(pointsx1))]
    #key_2 = [(0 for i in range(2)) for i in range(len(pointsx2))]
    for i in range (0, len(pointsx1)):
        key1[i][0] = pointsx1[i]
        key1[i][1] = pointsy1[i]
    for i in range (0, len(pointsx1)):
        key2[i][0] = pointsx2[i]
        key2[i][1] = pointsy2[i]
    '''
    '''
    cv2.circle(frame1,(key1[0][0],key1[0][1]),1,(0,255,0),-1)
    cv2.circle(frame1,(key1[68][0],key1[68][1]),1,(0,255,0),-1)
    cv2.circle(frame1,(key1[78][0],key1[78][1]),1,(0,255,0),-1)
    
    cv2.imshow("faceDetecion", frame1)          
    c = cv2.waitKey(0)     
    cv2.destroyAllWindows() 
    '''
    #SrcPoints = np.float32([key2[0],key2[68],key2[78]])
    #CanvasPoints = np.float32([key1[0],key1[68],key1[78]])   
    
    pt1 = findaffine(kpath1)
    pt2 = findaffine(kpath2)
    
    SrcPoints = [[pt2[0],pt2[1]],[pt2[2],pt2[3]],[pt2[4],pt2[5]]]
    CanvasPoints = [[pt1[0],pt1[1]],[pt1[2],pt1[3]],[pt1[4],pt1[5]]]
    
    #SrcPoints = [key2[0],key2[68],key2[78]]
    #CanvasPoints = [key1[0],key1[68],key1[78]]
    
    #for i in SrcPoints:
    #    drawPoints(Img, i.reshape(-1, 1), (0,255,0), radius=1)  
    #SrcPointsA = np.array(SrcPoints, dtype=np.float32)
    #CanvasPointsA = np.array(CanvasPoints, dtype=np.float32)
    
    SrcPointsA = np.asarray(SrcPoints, dtype=np.float32)
    CanvasPointsA = np.asarray(CanvasPoints, dtype=np.float32)
    print ('SrcPoints:')
    print (SrcPointsA)
    print ('CanvasPoints:')
    print (CanvasPointsA)
    AffineMatrix = cv2.getAffineTransform(np.array(SrcPointsA),np.array(CanvasPointsA))
    #print ('AffineMatrix:\n', AffineMatrix)
    AffineImg = cv2.warpAffine(Img, AffineMatrix, (Img.shape[1], Img.shape[0]))

    return AffineImg  
        
if __name__ == '__main__':
    
    filename = 'E:\\MyProject\\S5_GANPart\\test'  
    filename1 = 'unify2.jpg'
    filename2 = 'Ella Wahlestedt_A.jpg'
    filepath1 = os.path.join(filename, filename1)
    filepath2 = os.path.join(filename, filename2)
    
    SrcImg = cv2.imread(filepath2)
    Img = SrcImg
    AffineImg = getAffine(filepath1, filepath2, filepath1+".json", filepath2+".json")
    cv2.imshow('Src', Img)
    cv2.imshow('AffineImg', AffineImg)
    lefty, righty, leftx, rightx= 300, 800, 200, 700
    face = AffineImg[lefty:righty, leftx:rightx]     
    cv2.imshow('face', face)
    cv2.imwrite('E:/MyProject/S5_GANPart/test/data/one/face.png', face)
    c = cv2.waitKey(0)     
    cv2.destroyAllWindows() 
     