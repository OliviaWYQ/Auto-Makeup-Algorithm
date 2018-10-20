import requests  
#import tensorflow as tf
import json
from json import JSONDecoder  
import cv2  
import os  
import itertools
import numpy as np
from matplotlib import pyplot as plt


def findpoints(filepath):
    with open(filepath+".json",'r') as load_f:
        req_dict = json.load(load_f)
    
    #print ("face number =",len(req_dict[u'faces']))  
    face_num = len(req_dict[u'faces'])  
    frame = cv2.imread(filepath)
    '''
    img = cv2.imread(filepath, -1)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgLap = cv2.Laplacian(imgGray,cv2.CV_8U)
    '''
    #threshold,imgOtsu = cv2.threshold(imgGray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #imgAdapt = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    
    #frame=imgLap
    
    lx=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    ly=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    rx=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    ry=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lmx=[0,0,0,0,0,0,0,0,0,0] 
    lmy=[0,0,0,0,0,0,0,0,0,0]
    rmx=[0,0,0,0,0,0,0,0,0,0,0,0] 
    rmy=[0,0,0,0,0,0,0,0,0,0,0,0]
    nx=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    ny=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lex=[0,0,0,0,0,0,0,0,0,0,0] 
    ley=[0,0,0,0,0,0,0,0,0,0,0]
    rex=[0,0,0,0,0,0,0,0,0,0,0]
    rey=[0,0,0,0,0,0,0,0,0,0,0]
    lbx=[0,0,0,0,0,0,0,0,0,0] 
    lby=[0,0,0,0,0,0,0,0,0,0]
    rbx=[0,0,0,0,0,0,0,0,0,0] 
    rby=[0,0,0,0,0,0,0,0,0,0]
    
    for i in range(face_num):  
        #print ("person:", face_num)
        point = req_dict[u'faces'][i][u'landmark'] 
        #print(point)  
        cx=point[u'contour_chin'][u'x'] 
        cy=point[u'contour_chin'][u'y']
        
        lx[1]=point[u'contour_left1'][u'x']
        lx[2]=point[u'contour_left2'][u'x']
        lx[3]=point[u'contour_left3'][u'x']
        lx[4]=point[u'contour_left4'][u'x']
        lx[5]=point[u'contour_left5'][u'x']
        lx[6]=point[u'contour_left6'][u'x']
        lx[7]=point[u'contour_left7'][u'x']
        lx[8]=point[u'contour_left8'][u'x']
        lx[9]=point[u'contour_left9'][u'x']
        lx[10]=point[u'contour_left10'][u'x']
        lx[11]=point[u'contour_left11'][u'x']
        lx[12]=point[u'contour_left12'][u'x']
        lx[13]=point[u'contour_left13'][u'x']
        lx[14]=point[u'contour_left14'][u'x']
        lx[15]=point[u'contour_left15'][u'x']
        lx[16]=point[u'contour_left16'][u'x']
        
        ly[1]=point[u'contour_left1'][u'y'] 
        ly[2]=point[u'contour_left2'][u'y']
        ly[3]=point[u'contour_left3'][u'y']
        ly[4]=point[u'contour_left4'][u'y']
        ly[5]=point[u'contour_left5'][u'y']
        ly[6]=point[u'contour_left6'][u'y']
        ly[7]=point[u'contour_left7'][u'y']
        ly[8]=point[u'contour_left8'][u'y']
        ly[9]=point[u'contour_left9'][u'y']
        ly[10]=point[u'contour_left10'][u'y']
        ly[11]=point[u'contour_left11'][u'y']
        ly[12]=point[u'contour_left12'][u'y']
        ly[13]=point[u'contour_left13'][u'y']
        ly[14]=point[u'contour_left14'][u'y']
        ly[15]=point[u'contour_left15'][u'y']
        ly[16]=point[u'contour_left16'][u'y']
        
        
        rx[1]=point[u'contour_right1'][u'x'] 
        rx[2]=point[u'contour_right2'][u'x']
        rx[3]=point[u'contour_right3'][u'x']
        rx[4]=point[u'contour_right4'][u'x']
        rx[5]=point[u'contour_right5'][u'x']
        rx[6]=point[u'contour_right6'][u'x']
        rx[7]=point[u'contour_right7'][u'x']
        rx[8]=point[u'contour_right8'][u'x']
        rx[9]=point[u'contour_right9'][u'x']
        rx[10]=point[u'contour_right10'][u'x']
        rx[11]=point[u'contour_right11'][u'x']
        rx[12]=point[u'contour_right12'][u'x']
        rx[13]=point[u'contour_right13'][u'x']
        rx[14]=point[u'contour_right14'][u'x']
        rx[15]=point[u'contour_right15'][u'x']
        rx[16]=point[u'contour_right16'][u'x']
        
        ry[1]=point[u'contour_right1'][u'y']
        ry[2]=point[u'contour_right2'][u'y']
        ry[3]=point[u'contour_right3'][u'y']
        ry[4]=point[u'contour_right4'][u'y']
        ry[5]=point[u'contour_right5'][u'y']
        ry[6]=point[u'contour_right6'][u'y']
        ry[7]=point[u'contour_right7'][u'y']
        ry[8]=point[u'contour_right8'][u'y']
        ry[9]=point[u'contour_right9'][u'y']
        ry[10]=point[u'contour_right10'][u'y']
        ry[11]=point[u'contour_right11'][u'y']
        ry[12]=point[u'contour_right12'][u'y']
        ry[13]=point[u'contour_right13'][u'y']
        ry[14]=point[u'contour_right14'][u'y']
        ry[15]=point[u'contour_right15'][u'y']
        ry[16]=point[u'contour_right16'][u'y']
        
        
        lmx[1]=point[u'mouth_lower_lip_top'][u'x']
        lmx[2]=point[u'mouth_lower_lip_left_contour1'][u'x']
        lmx[3]=point[u'mouth_left_corner'][u'x'] 
        lmx[4]=point[u'mouth_lower_lip_left_contour2'][u'x']
        lmx[5]=point[u'mouth_lower_lip_left_contour3'][u'x']
        lmx[6]=point[u'mouth_lower_lip_bottom'][u'x']
        lmx[7]=point[u'mouth_lower_lip_right_contour3'][u'x']
        lmx[8]=point[u'mouth_lower_lip_right_contour2'][u'x']
        lmx[9]=point[u'mouth_lower_lip_right_contour1'][u'x']
        
        
        lmy[1]=point[u'mouth_lower_lip_top'][u'y']
        lmy[2]=point[u'mouth_lower_lip_left_contour1'][u'y']
        lmy[3]=point[u'mouth_left_corner'][u'y']
        lmy[4]=point[u'mouth_lower_lip_left_contour2'][u'y']
        lmy[5]=point[u'mouth_lower_lip_left_contour3'][u'y']
        lmy[6]=point[u'mouth_lower_lip_bottom'][u'y']
        lmy[7]=point[u'mouth_lower_lip_right_contour3'][u'y']
        lmy[8]=point[u'mouth_lower_lip_right_contour2'][u'y']
        lmy[9]=point[u'mouth_lower_lip_right_contour1'][u'y']
        
    
        rmx[1]=point[u'mouth_upper_lip_left_contour1'][u'x']
        rmx[2]=point[u'mouth_upper_lip_left_contour2'][u'x']
        rmx[3]=point[u'mouth_upper_lip_left_contour3'][u'x']
        rmx[4]=point[u'mouth_upper_lip_left_contour4'][u'x']
        rmx[5]=point[u'mouth_upper_lip_bottom'][u'x']
        rmx[6]=point[u'mouth_upper_lip_right_contour4'][u'x']
        rmx[7]=point[u'mouth_upper_lip_right_contour3'][u'x']
        rmx[8]=point[u'mouth_right_corner'][u'x']
        rmx[9]=point[u'mouth_upper_lip_right_contour2'][u'x']
        rmx[10]=point[u'mouth_upper_lip_right_contour1'][u'x']
        rmx[11]=point[u'mouth_upper_lip_top'][u'x']
        
        rmy[1]=point[u'mouth_upper_lip_left_contour1'][u'y']
        rmy[2]=point[u'mouth_upper_lip_left_contour2'][u'y']
        rmy[3]=point[u'mouth_upper_lip_left_contour3'][u'y']
        rmy[4]=point[u'mouth_upper_lip_left_contour4'][u'y']
        rmy[5]=point[u'mouth_upper_lip_bottom'][u'y']
        rmy[6]=point[u'mouth_upper_lip_right_contour4'][u'y']
        rmy[7]=point[u'mouth_upper_lip_right_contour3'][u'y']
        rmy[8]=point[u'mouth_right_corner'][u'y']
        rmy[9]=point[u'mouth_upper_lip_right_contour2'][u'y']
        rmy[10]=point[u'mouth_upper_lip_right_contour1'][u'y']
        rmy[11]=point[u'mouth_upper_lip_top'][u'y']
        
         
        nx[1]=point[u'nose_left_contour1'][u'x'] 
        nx[2]=point[u'nose_left_contour2'][u'x'] 
        nx[3]=point[u'nose_left_contour3'][u'x'] 
        nx[4]=point[u'nose_left_contour4'][u'x'] 
        nx[5]=point[u'nose_left_contour5'][u'x'] 
        nx[6]=point[u'nose_middle_contour'][u'x'] 
        nx[7]=point[u'nose_right_contour1'][u'x'] 
        nx[8]=point[u'nose_right_contour2'][u'x'] 
        nx[9]=point[u'nose_right_contour3'][u'x'] 
        nx[10]=point[u'nose_right_contour4'][u'x'] 
        nx[11]=point[u'nose_right_contour5'][u'x'] 
        nx[12]=point[u'nose_bridge1'][u'x']
        nx[13]=point[u'nose_bridge2'][u'x']
        nx[14]=point[u'nose_bridge3'][u'x']
        nx[15]=point[u'nose_tip'][u'x'] 
        
        ny[1]=point[u'nose_left_contour1'][u'y'] 
        ny[2]=point[u'nose_left_contour2'][u'y'] 
        ny[3]=point[u'nose_left_contour3'][u'y'] 
        ny[4]=point[u'nose_left_contour4'][u'y'] 
        ny[5]=point[u'nose_left_contour5'][u'y'] 
        ny[6]=point[u'nose_middle_contour'][u'y'] 
        ny[7]=point[u'nose_right_contour1'][u'y'] 
        ny[8]=point[u'nose_right_contour2'][u'y'] 
        ny[9]=point[u'nose_right_contour3'][u'y'] 
        ny[10]=point[u'nose_right_contour4'][u'y'] 
        ny[11]=point[u'nose_right_contour5'][u'y'] 
        ny[12]=point[u'nose_bridge1'][u'y']
        ny[13]=point[u'nose_bridge2'][u'y']
        ny[14]=point[u'nose_bridge3'][u'y']
        ny[15]=point[u'nose_tip'][u'y']
        
        
        lex[1]=point[u'left_eye_center'][u'x']
        lex[2]=point[u'left_eye_pupil'][u'x']
        lex[3]=point[u'left_eye_left_corner'][u'x']
        lex[4]=point[u'left_eye_lower_left_quarter'][u'x']
        lex[5]=point[u'left_eye_bottom'][u'x'] 
        lex[6]=point[u'left_eye_lower_right_quarter'][u'x']
        lex[7]=point[u'left_eye_right_corner'][u'x']
        lex[8]=point[u'left_eye_upper_right_quarter'][u'x']
        lex[9]=point[u'left_eye_top'][u'x']
        lex[10]=point[u'left_eye_upper_left_quarter'][u'x']
        
        ley[1]=point[u'left_eye_center'][u'y']
        ley[2]=point[u'left_eye_pupil'][u'y']
        ley[3]=point[u'left_eye_left_corner'][u'y']
        ley[4]=point[u'left_eye_lower_left_quarter'][u'y']
        ley[5]=point[u'left_eye_bottom'][u'y'] 
        ley[6]=point[u'left_eye_lower_right_quarter'][u'y']
        ley[7]=point[u'left_eye_right_corner'][u'y']
        ley[8]=point[u'left_eye_upper_right_quarter'][u'y']
        ley[9]=point[u'left_eye_top'][u'y']
        ley[10]=point[u'left_eye_upper_left_quarter'][u'y']
      
        rex[1]=point[u'right_eye_center'][u'x']
        rex[2]=point[u'right_eye_pupil'][u'x']
        rex[3]=point[u'right_eye_left_corner'][u'x']
        rex[4]=point[u'right_eye_lower_left_quarter'][u'x']
        rex[5]=point[u'right_eye_bottom'][u'x'] 
        rex[6]=point[u'right_eye_lower_right_quarter'][u'x']
        rex[7]=point[u'right_eye_right_corner'][u'x']
        rex[8]=point[u'right_eye_upper_right_quarter'][u'x']
        rex[9]=point[u'right_eye_top'][u'x']
        rex[10]=point[u'right_eye_upper_left_quarter'][u'x']
    
        rey[1]=point[u'right_eye_center'][u'y']
        rey[2]=point[u'right_eye_pupil'][u'y']
        rey[3]=point[u'right_eye_left_corner'][u'y']
        rey[4]=point[u'right_eye_lower_left_quarter'][u'y']
        rey[5]=point[u'right_eye_bottom'][u'y'] 
        rey[6]=point[u'right_eye_lower_right_quarter'][u'y']
        rey[7]=point[u'right_eye_right_corner'][u'y']
        rey[8]=point[u'right_eye_upper_right_quarter'][u'y']
        rey[9]=point[u'right_eye_top'][u'y']
        rey[10]=point[u'right_eye_upper_left_quarter'][u'y']
        
        lbx[1]=point[u'left_eyebrow_left_corner'][u'x'] 
        lbx[2]=point[u'left_eyebrow_lower_left_quarter'][u'x']
        lbx[3]=point[u'left_eyebrow_lower_middle'][u'x']
        lbx[4]=point[u'left_eyebrow_lower_right_quarter'][u'x']
        lbx[5]=point[u'left_eyebrow_lower_right_corner'][u'x']
        lbx[6]=point[u'left_eyebrow_upper_right_corner'][u'x']
        lbx[7]=point[u'left_eyebrow_upper_right_quarter'][u'x']
        lbx[8]=point[u'left_eyebrow_upper_middle'][u'x']
        lbx[9]=point[u'left_eyebrow_upper_left_quarter'][u'x']
        
        lby[1]=point[u'left_eyebrow_left_corner'][u'y'] 
        lby[2]=point[u'left_eyebrow_lower_left_quarter'][u'y']
        lby[3]=point[u'left_eyebrow_lower_middle'][u'y']
        lby[4]=point[u'left_eyebrow_lower_right_quarter'][u'y']
        lby[5]=point[u'left_eyebrow_lower_right_corner'][u'y']
        lby[6]=point[u'left_eyebrow_upper_right_corner'][u'y']
        lby[7]=point[u'left_eyebrow_upper_right_quarter'][u'y']
        lby[8]=point[u'left_eyebrow_upper_middle'][u'y']
        lby[9]=point[u'left_eyebrow_upper_left_quarter'][u'y']
        
        rbx[1]=point[u'right_eyebrow_upper_left_corner'][u'x']
        rbx[2]=point[u'right_eyebrow_lower_left_corner'][u'x']
        rbx[3]=point[u'right_eyebrow_lower_left_quarter'][u'x']
        rbx[4]=point[u'right_eyebrow_lower_middle'][u'x']
        rbx[5]=point[u'right_eyebrow_lower_right_quarter'][u'x']
        rbx[6]=point[u'right_eyebrow_right_corner'][u'x']
        rbx[7]=point[u'right_eyebrow_upper_right_quarter'][u'x']
        rbx[8]=point[u'right_eyebrow_upper_middle'][u'x']
        rbx[9]=point[u'right_eyebrow_upper_left_quarter'][u'x']
        
        rby[1]=point[u'right_eyebrow_upper_left_corner'][u'y'] 
        rby[2]=point[u'right_eyebrow_lower_left_corner'][u'y']
        rby[3]=point[u'right_eyebrow_lower_left_quarter'][u'y']
        rby[4]=point[u'right_eyebrow_lower_middle'][u'y']
        rby[5]=point[u'right_eyebrow_lower_right_quarter'][u'y']
        rby[6]=point[u'right_eyebrow_right_corner'][u'y']
        rby[7]=point[u'right_eyebrow_upper_right_quarter'][u'y']
        rby[8]=point[u'right_eyebrow_upper_middle'][u'y']
        rby[9]=point[u'right_eyebrow_upper_left_quarter'][u'y']
        
         
        
        for j in range (15):
            cv2.line(frame,(lx[j+1],ly[j+1]),(lx[j+2],ly[j+2]),(255,0,0),1)  
            cv2.line(frame,(rx[j+1],ry[j+1]),(rx[j+2],ry[j+2]),(255,0,0),1)  
            
        for j in range (5):
            cv2.line(frame,(nx[j+1],ny[j+1]),(nx[j+2],ny[j+2]),(255,0,0),1)  
        for j in range (11, 14, 1):
            cv2.line(frame,(nx[j+1],ny[j+1]),(nx[j+2],ny[j+2]),(255,0,0),1) 
        for j in range (6, 10, 1):
            cv2.line(frame,(nx[j+1],ny[j+1]),(nx[j+2],ny[j+2]),(255,0,0),1) 
            
        cv2.line(frame,(nx[6],ny[6]),(nx[10],ny[10]),(255,0,0),1) 
        cv2.line(frame,(lx[16],ly[16]),(cx,cy),(255,0,0),1)  
        cv2.line(frame,(rx[16],ry[16]),(cx,cy),(255,0,0),1)  
        
        for j in range (3, 10, 1):
            cv2.line(frame,(lex[j],ley[j]),(lex[j+1],ley[j+1]),(255,0,0),1)  
            cv2.line(frame,(rex[j],rey[j]),(rex[j+1],rey[j+1]),(255,0,0),1)  
            
        cv2.line(frame,(lex[3],ley[3]),(lex[10],ley[10]),(255,0,0),1)  
        cv2.line(frame,(rex[3],rey[3]),(rex[10],rey[10]),(255,0,0),1)  
        
        for j in range (8):
            cv2.line(frame,(lbx[j+1],lby[j+1]),(lbx[j+2],lby[j+2]),(255,0,0),1)  
            cv2.line(frame,(rbx[j+1],rby[j+1]),(rbx[j+2],rby[j+2]),(255,0,0),1)  
        cv2.line(frame,(lbx[1],lby[1]),(lbx[9],lby[9]),(255,0,0),1)  
        cv2.line(frame,(rbx[1],rby[1]),(rbx[9],rby[9]),(255,0,0),1)  
        
        for j in range (7):
            cv2.line(frame,(lmx[j+1],lmy[j+1]),(lmx[j+2],lmy[j+2]),(255,0,0),1)  
        for j in range (2, 10, 1):
            cv2.line(frame,(rmx[j+1],rmy[j+1]),(rmx[j+2],rmy[j+2]),(255,0,0),1)  
        
        cv2.line(frame,(lmx[8],lmy[8]),(rmx[8],rmy[8]),(255,0,0),1)
        cv2.line(frame,(lmx[1],lmy[1]),(lmx[9],lmy[9]),(255,0,0),1)
        cv2.line(frame,(lmx[9],lmy[9]),(rmx[8],rmy[8]),(255,0,0),1)  
        cv2.line(frame,(rmx[1],rmy[1]),(rmx[11],rmy[11]),(255,0,0),1)  
        cv2.line(frame,(rmx[1],rmy[1]),(rmx[2],rmy[2]),(255,0,0),1)  
        cv2.line(frame,(lmx[3],lmy[3]),(rmx[2],rmy[2]),(255,0,0),1)  
        cv2.line(frame,(lmx[3],lmy[3]),(rmx[3],rmy[3]),(255,0,0),1)  
        
    
        cv2.circle(frame,(cx,cy),1,(0,255,0),-1)
        for j in range (16):
            cv2.circle(frame,(lx[j+1],ly[j+1]),1,(0,255,0),-1)
            cv2.circle(frame,(rx[j+1],ry[j+1]),1,(0,255,0),-1)
        for j in range (9):    
            cv2.circle(frame,(lmx[j+1],lmy[j+1]),1,(0,255,0),-1)
        for j in range (11): 
            cv2.circle(frame,(rmx[j+1],rmy[j+1]),1,(0,255,0),-1)
        for j in range (15):    
            cv2.circle(frame,(nx[j+1],ny[j+1]),1,(0,255,0),-1)
        for j in range (10):    
            cv2.circle(frame,(lex[j+1],ley[j+1]),1,(0,255,0),-1)
        for j in range (10):    
            cv2.circle(frame,(rex[j+1],rey[j+1]),1,(0,255,0),-1)
        for j in range (9):    
            cv2.circle(frame,(lbx[j+1],lby[j+1]),1,(0,255,0),-1)
        for j in range (9):    
            cv2.circle(frame,(rbx[j+1],rby[j+1]),1,(0,255,0),-1)


        lx.remove(0);rx.remove(0);lmx.remove(0);rmx.remove(0);nx.remove(0);lex.remove(0);rex.remove(0);lbx.remove(0);rbx.remove(0)
        ly.remove(0);ry.remove(0);lmy.remove(0);rmy.remove(0);ny.remove(0);ley.remove(0);rey.remove(0);lby.remove(0);rby.remove(0)
        pointsx=itertools.chain([cx],lx,rx,lmx,rmx,nx,lex,rex,lbx,rbx)
        pointsy=itertools.chain([cy],ly,ry,lmy,rmy,ny,ley,rey,lby,rby)
        pointsx1=list(pointsx)
        pointsy1=list(pointsy)
        
        return pointsx1, pointsy1
        #print (pointsx1,'\n',pointsy1)
        #print (len(pointsx1))
        
        '''
        cv2.imwrite("mask_"+filename2,frame) 
        cv2.imshow("faceDetecion", frame)          
        c = cv2.waitKey(0)     
        cv2.destroyAllWindows()   
        '''
        
def findaffine(jsonpath):
    with open(jsonpath,'r') as load_f:
        req_dict = json.load(load_f)
    face_num = len(req_dict[u'faces'])  
    for i in range(face_num):  
        point = req_dict[u'faces'][i][u'landmark'] 
        c_x=point[u'contour_chin'][u'x'] 
        c_y=point[u'contour_chin'][u'y']
        le_x=point[u'left_eye_center'][u'x']
        le_y=point[u'left_eye_center'][u'y']  
        re_x=point[u'right_eye_center'][u'x']
        re_y=point[u'right_eye_center'][u'y']
    
    return c_x, c_y, le_x, le_y, re_x, re_y
    
def main(_):

    filename = 'E:\\MyProject\\S5_GANPart\\tf04'  
    filename2 = 'Amanda Seyfried_B_0.jpg'
    filepath = os.path.join(filename, filename2)
    pointsx1, pointsy1 = findpoints(filepath)
    key = [[0 for i in range(2)] for i in range(len(pointsx1))]
    
    for i in range (0, len(pointsx1)):
        key[i][0] = pointsx1[i]
        key[i][1] = pointsy1[i]
    print (key)
    
if __name__ == '__main__':
    tf.app.run()
    
    
    