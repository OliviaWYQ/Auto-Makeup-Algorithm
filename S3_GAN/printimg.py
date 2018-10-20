# -*- coding: utf-8 -*-
#import tensorflow as tf
import numpy as np
import os
import cv2  
import PIL.Image as Image
from facemask import findpoints
from affine import getAffine
from method import *
from savedata import img2data

if __name__ == '__main__':
    
    filename = 'E:\\MyProject\\S5_GANPart\\tf04'  
    filename1 = 'Amanda Seyfried_A_0.jpg'
    filename2 = 'Amanda Seyfried_B_0.jpg'
    filepath1 = os.path.join(filename, filename1)
    filepath2 = os.path.join(filename, filename2)
    frame1 = cv2.imread(os.path.join(filename, filename1))
    frame2 = cv2.imread(filepath2)
    pointsx1, pointsy1 = findpoints(filepath1)
    pointsx2, pointsy2 = findpoints(filepath2)
    key1 = [[0 for i in range(2)] for i in range(len(pointsx1))]
    key2 = [[0 for i in range(2)] for i in range(len(pointsx2))]
    key_1 = [(0 for i in range(2)) for i in range(len(pointsx1))]
    key_2 = [(0 for i in range(2)) for i in range(len(pointsx2))]
    key11 = [[0 for i in range(2)] for i in range(len(pointsx1)+8+20)]
    key22 = [[0 for i in range(2)] for i in range(len(pointsx1)+8+20)]
    
    for i in range (0, len(pointsx1)):
        key1[i][1] = pointsx1[i]
        key1[i][0] = pointsy1[i]
        key11[i] = key1[i]
        key22[i] = key2[i]
    #print (key)
    for i in range (0, len(pointsx1)):
        key2[i][1] = pointsx2[i]
        key2[i][0] = pointsy2[i]
        key_1[i] = tuple(key1[i])
        key_2[i] = tuple(key2[i])

    '''
    L = len(pointsx1)
    dx = [[0 for i in range(L)] for i in range(L)]
    for i in range (0, L): 
        for k in range (0, L):
            dx[i][k] = 1/2 * (pointsx1[i]+pointsx1[i+k])
    print (np.shape(dx))
    '''
    AffineImg = getAffine(filepath1, filepath2)
    transfile = 'Affine.png'
    cv2.imwrite(transfile, AffineImg)
    data = img2data(os.path.join(filename, transfile))
    np.savetxt('data2.txt', data, fmt='%s', newline='\n')
    a4 = readData('Amanda Seyfried_A_0.txt')
    e4 = readData('data2.txt')
                
    width = 256
    height = 256
    length = width * height
    
    '''
    r = [0] * length
    g = [0] * length
    b = [0] * length
    for i in range (0, length):
        r[i] = a4[i][0]
        g[i] = a4[i][1]
        b[i] = a4[i][2]
    print (np.shape(r))
    '''
    data = np.zeros((width, height, 3), dtype=np.uint8)
    data2 = np.zeros((width, height, 3), dtype=np.uint8)
    data3 = np.zeros((width, height, 3), dtype=np.uint8)
    data4 = np.zeros((width, height, 3), dtype=np.uint8)
    data5 = np.zeros((width, height, 3), dtype=np.uint8)
    data6 = np.zeros((width, height, 3), dtype=np.uint8)
    #print (np.shape(data))
    #print (len(key1))
    addpoint(key11)
    addpoint(key22)
    
    for i in range (0, length-1):
        x = int (i/width)
        y = i % width
        data[x, y] = meanMethod(a4[i],a4[i])
        data2[x, y] = meanMethod(e4[i],e4[i])
        data3[x, y] = meanMethod(a4[i],e4[i])
        data4[x, y] = [0,0,0]
        #data4[x, y] = data[x, y]
        data5[x, y] = [0,0,0]
        data6[x, y] = [1,1,1]
    
    n=8
    
    printOriPoint(data4, data2, key11, key11, n)
    
    img = Image.fromarray(data4, 'RGB')
    img.save('output.png')
    img.show()




