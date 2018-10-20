# -*- coding: utf-8 -*-
from PIL import Image  
import os

path = 'E:\\MyProject\\S5_GANPart\\test\\data\\checked\\aff_B' 
files= os.listdir(path)
for file in files: 
    filename = os.path.split(file)[1]
    filepath = path+'\\'+filename
    img = Image.open(filepath)  
    new_img= img.resize((512, 512),Image.ANTIALIAS) # w代表宽度，h代表高度，最后一个参数指	定采用的算法  
    new_img.save('E:\\MyProject\\S5_GANPart\\test\\data\\checked\\aff_B_512\\'+filename,quality=100)