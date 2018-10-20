# -*- coding: utf-8 -*-
import os
from affine import getAffine
import cv2
imgpathA = 'E:\\MyProject\\S5_GANPart\\tf04\\data\\western_A'
imgpathB = 'E:\\MyProject\\S5_GANPart\\tf04\\data\\western_B'
pathA = 'E:\\MyProject\\S5_GANPart\\tf04\\data\\json_western_A'
pathB = 'E:\\MyProject\\S5_GANPart\\tf04\\data\\json_western_B'
            
for dirpath, dirs, files in os.walk('./data/western_A'):
    for file in files:    
        filename = os.path.split(file)[1]
        name = filename.split('_')[0]
        #arg = filename.split('_')[1]
        
        if os.path.splitext(file)[1] == '.jpg':   
            #print (filename)
            #os.rename(pathA+'\\'+file, pathA+'\\'+name+'_A.jpg'+'.json')
            
            #outpath = os.path.join("E:\\MyProject\\S5_GANPart\\tf04\\data\\affine", filename)
            filepath1 = 'E:\\MyProject\\S5_GANPart\\tf04\\unify.jpg'
            filepath2 = os.path.join(imgpathA, name + '_A' +'.jpg')
            kpath1 = 'E:\\MyProject\\S5_GANPart\\tf04\\unify.jpg'
            kpath2 = os.path.join(pathA, name + '_A' +'.jpg')
            #print (filepath1)
            #print (filepath2)
            #print (kpath1)
            #print (kpath2)
            #print (outpath)
            
            AffineImg = getAffine(filepath1, filepath2, kpath1+".json", kpath2+".json")
            lefty, righty, leftx, rightx= 147, 422, 58, 333
            face = AffineImg[lefty:righty, leftx:rightx]     
            cv2.imwrite('E:\\MyProject\\S5_GANPart\\tf04\\data\\aff_A'+'\\'+filename, face)
            #cv2.imwrite(filename, AffineImg)
            
            