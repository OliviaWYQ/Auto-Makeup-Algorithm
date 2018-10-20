# -*-coding:utf-8-*-
from PIL import Image
import pylab as plb
import os
from skimage import data_dir,io

path = 'E:\MyProject\S1_TrainingData\S1_Compare\western'

"""
#显示文件夹内所有文件名
s = os.sep
root = 'E:\MyProject\S1_TrainingData\S1_Compare\western'
for i in os.listdir(root):
    if os.path.isfile(os.path.join(root,i)):
        print (i)

"""
"""
#显示文件数量
str=path + '/*.jpg'
coll = io.ImageCollection(str)
print(len(coll))
"""

for(path,dirs,files) in os.walk(path):                        # 读取文件
    #dirs =  os.listdir(path)
    for f in files:  
        #print (file)
            
        #im = Image.open("Gisele Bündchen.jpg")
        #file = 'Gisele Bündchen.jpg'
        file_path = path+'\\'+ f
        #print (file_path)
        (filepath,tempfilename) = os.path.split(file_path)
        (filename,extension) = os.path.splitext(tempfilename)
        #print (filename,extension)
        
        im = Image.open(file_path)
        
        # 截取图片A
        x = 0
        y = 0
        w = 400
        h = 600
        region = im.crop((x, y, x+w, y+h))
        #region.save(filename+"_A.jpg")
        filename_A = filename+"_A.jpg"
        pre_savename_A = 'E:\MyProject\S1_TrainingData\S1_Compare\western_A'
        path_A = os.path.join(pre_savename_A,filename_A)
        print (path_A)
        region.save(path_A)
        
        #截取图片B
        x = 400
        y = 0
        w = 400
        h = 600
        region = im.crop((x, y, x+w, y+h))
        #region.save(filename+"_B.jpg")
        filename_B = filename+"_B.jpg"
        pre_savename_B = 'E:\MyProject\S1_TrainingData\S1_Compare\western_B'
        path_B = os.path.join(pre_savename_B,filename_B)
        print (path_B)
        region.save(path_B)
        
        
        
        
        
        
        
        
