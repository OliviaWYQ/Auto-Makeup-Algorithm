import requests  
from json import JSONDecoder  
import cv2  
import os  

http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"  
key =""
secret =""      
  
filename = 'E:\MyProject\S2_MarkingPoint'  
filename2 = 'Amanda Seyfried_B-0.jpg'
filepath = os.path.join(filename, filename2)
data = {"api_key":key, "api_secret":secret, "return_landmark":"1"}  
files = {"image_file":open(filepath, "rb")}  
response = requests.post(http_url, data=data, files=files)  
req_con = response.content.decode('utf-8')  
req_dict = JSONDecoder().decode(req_con)  
#print (req_dict)

print "face number =",len(req_dict[u'faces'])  
face_num = len(req_dict[u'faces'])  
frame = cv2.imread(filepath)

lx=[0,0,0,0,0,0,0,0,0,0] #左脸
ly=[0,0,0,0,0,0,0,0,0,0]
rx=[0,0,0,0,0,0,0,0,0,0] #右脸
ry=[0,0,0,0,0,0,0,0,0,0]
dmx=[0,0,0,0,0,0,0,0,0,0] #下嘴
dmy=[0,0,0,0,0,0,0,0,0,0]
umx=[0,0,0,0,0,0,0,0,0,0] #上嘴
umy=[0,0,0,0,0,0,0,0,0,0]
nx=[0,0,0,0,0,0,0,0,0,0,0] #鼻子
ny=[0,0,0,0,0,0,0,0,0,0,0]
lex=[0,0,0,0,0,0,0,0,0,0,0] #左眼
ley=[0,0,0,0,0,0,0,0,0,0,0]
rex=[0,0,0,0,0,0,0,0,0,0,0] #右眼
rey=[0,0,0,0,0,0,0,0,0,0,0]
lbx=[0,0,0,0,0,0,0,0,0] #左眉
lby=[0,0,0,0,0,0,0,0,0]
rbx=[0,0,0,0,0,0,0,0,0] #右眉
rby=[0,0,0,0,0,0,0,0,0]


for i in range(face_num):  
    point = req_dict[u'faces'][i][u'landmark'] 
    #print(point)  
    cx=point[u'contour_chin'][u'x'] #下巴
    cy=point[u'contour_chin'][u'y']
    
    lx[1]=point[u'contour_left1'][u'x'] #左脸
    lx[2]=point[u'contour_left2'][u'x']
    lx[3]=point[u'contour_left3'][u'x']
    lx[4]=point[u'contour_left4'][u'x']
    lx[5]=point[u'contour_left5'][u'x']
    lx[6]=point[u'contour_left6'][u'x']
    lx[7]=point[u'contour_left7'][u'x']
    lx[8]=point[u'contour_left8'][u'x']
    lx[9]=point[u'contour_left9'][u'x']
    
    ly[1]=point[u'contour_left1'][u'y'] 
    ly[2]=point[u'contour_left2'][u'y']
    ly[3]=point[u'contour_left3'][u'y']
    ly[4]=point[u'contour_left4'][u'y']
    ly[5]=point[u'contour_left5'][u'y']
    ly[6]=point[u'contour_left6'][u'y']
    ly[7]=point[u'contour_left7'][u'y']
    ly[8]=point[u'contour_left8'][u'y']
    ly[9]=point[u'contour_left9'][u'y']
    
    rx[1]=point[u'contour_right1'][u'x'] #右脸
    rx[2]=point[u'contour_right2'][u'x']
    rx[3]=point[u'contour_right3'][u'x']
    rx[4]=point[u'contour_right4'][u'x']
    rx[5]=point[u'contour_right5'][u'x']
    rx[6]=point[u'contour_right6'][u'x']
    rx[7]=point[u'contour_right7'][u'x']
    rx[8]=point[u'contour_right8'][u'x']
    rx[9]=point[u'contour_right9'][u'x']
    
    ry[1]=point[u'contour_right1'][u'y']
    ry[2]=point[u'contour_right2'][u'y']
    ry[3]=point[u'contour_right3'][u'y']
    ry[4]=point[u'contour_right4'][u'y']
    ry[5]=point[u'contour_right5'][u'y']
    ry[6]=point[u'contour_right6'][u'y']
    ry[7]=point[u'contour_right7'][u'y']
    ry[8]=point[u'contour_right8'][u'y']
    ry[9]=point[u'contour_right9'][u'y']
    
    
    dmx[1]=point[u'mouth_lower_lip_right_contour2'][u'x'] #下嘴
    dmx[2]=point[u'mouth_lower_lip_right_contour3'][u'x']   
    dmx[3]=point[u'mouth_lower_lip_bottom'][u'x']
    dmx[4]=point[u'mouth_lower_lip_left_contour3'][u'x']    
    dmx[5]=point[u'mouth_lower_lip_left_contour2'][u'x']
    dmx[6]=point[u'mouth_left_corner'][u'x'] 
    dmx[7]=point[u'mouth_lower_lip_left_contour1'][u'x']
    dmx[8]=point[u'mouth_lower_lip_top'][u'x']
    dmx[9]=point[u'mouth_lower_lip_right_contour1'][u'x']
    
    dmy[1]=point[u'mouth_lower_lip_right_contour2'][u'y']
    dmy[2]=point[u'mouth_lower_lip_right_contour3'][u'y']
    dmy[3]=point[u'mouth_lower_lip_bottom'][u'y']
    dmy[4]=point[u'mouth_lower_lip_left_contour3'][u'y']
    dmy[5]=point[u'mouth_lower_lip_left_contour2'][u'y']
    dmy[6]=point[u'mouth_left_corner'][u'y'] 
    dmy[7]=point[u'mouth_lower_lip_left_contour1'][u'y']
    dmy[8]=point[u'mouth_lower_lip_top'][u'y']
    dmy[9]=point[u'mouth_lower_lip_right_contour1'][u'y']
       
    umx[1]=point[u'mouth_upper_lip_left_contour3'][u'x'] #上嘴
    umx[2]=point[u'mouth_upper_lip_bottom'][u'x']
    umx[3]=point[u'mouth_upper_lip_right_contour3'][u'x']
    umx[4]=point[u'mouth_right_corner'][u'x'] 
    umx[5]=point[u'mouth_upper_lip_right_contour2'][u'x']
    umx[6]=point[u'mouth_upper_lip_right_contour1'][u'x']
    umx[7]=point[u'mouth_upper_lip_top'][u'x']
    umx[8]=point[u'mouth_upper_lip_left_contour1'][u'x']
    umx[9]=point[u'mouth_upper_lip_left_contour2'][u'x']
   
    umy[1]=point[u'mouth_upper_lip_left_contour3'][u'y']
    umy[2]=point[u'mouth_upper_lip_bottom'][u'y']
    umy[3]=point[u'mouth_upper_lip_right_contour3'][u'y']
    umy[4]=point[u'mouth_right_corner'][u'y'] 
    umy[5]=point[u'mouth_upper_lip_right_contour2'][u'y']
    umy[6]=point[u'mouth_upper_lip_right_contour1'][u'y'] 
    umy[7]=point[u'mouth_upper_lip_top'][u'y']     
    umy[8]=point[u'mouth_upper_lip_left_contour1'][u'y']
    umy[9]=point[u'mouth_upper_lip_left_contour2'][u'y']
   
    nx[1]=point[u'nose_contour_left1'][u'x'] #鼻子
    nx[2]=point[u'nose_contour_left2'][u'x'] 
    nx[3]=point[u'nose_left'][u'x'] 
    nx[4]=point[u'nose_contour_left3'][u'x'] 
    nx[5]=point[u'nose_contour_lower_middle'][u'x'] 
    nx[6]=point[u'nose_contour_right3'][u'x'] 
    nx[7]=point[u'nose_right'][u'x'] 
    nx[8]=point[u'nose_contour_right2'][u'x'] 
    nx[9]=point[u'nose_contour_right1'][u'x'] 
    nx[10]=point[u'nose_tip'][u'x'] 
    
    ny[1]=point[u'nose_contour_left1'][u'y'] #鼻子
    ny[2]=point[u'nose_contour_left2'][u'y'] 
    ny[3]=point[u'nose_left'][u'y']  
    ny[4]=point[u'nose_contour_left3'][u'y'] 
    ny[5]=point[u'nose_contour_lower_middle'][u'y'] 
    ny[6]=point[u'nose_contour_right3'][u'y'] 
    ny[7]=point[u'nose_right'][u'y'] 
    ny[8]=point[u'nose_contour_right2'][u'y'] 
    ny[9]=point[u'nose_contour_right1'][u'y'] 
    ny[10]=point[u'nose_tip'][u'y']
    
    lex[1]=point[u'left_eye_left_corner'][u'x'] #左眼
    lex[2]=point[u'left_eye_lower_left_quarter'][u'x']
    lex[3]=point[u'left_eye_bottom'][u'x'] 
    lex[4]=point[u'left_eye_lower_right_quarter'][u'x']
    lex[5]=point[u'left_eye_right_corner'][u'x']
    lex[6]=point[u'left_eye_upper_right_quarter'][u'x']
    lex[7]=point[u'left_eye_top'][u'x']
    lex[8]=point[u'left_eye_upper_left_quarter'][u'x']
    lex[9]=point[u'left_eye_center'][u'x']
    lex[10]=point[u'left_eye_pupil'][u'x']
    
    ley[1]=point[u'left_eye_left_corner'][u'y']
    ley[2]=point[u'left_eye_lower_left_quarter'][u'y']
    ley[3]=point[u'left_eye_bottom'][u'y'] 
    ley[4]=point[u'left_eye_lower_right_quarter'][u'y']
    ley[5]=point[u'left_eye_right_corner'][u'y']
    ley[6]=point[u'left_eye_upper_right_quarter'][u'y']
    ley[7]=point[u'left_eye_top'][u'y']
    ley[8]=point[u'left_eye_upper_left_quarter'][u'y']
    ley[9]=point[u'left_eye_center'][u'y']
    ley[10]=point[u'left_eye_pupil'][u'y']
    
    rex[1]=point[u'right_eye_right_corner'][u'x'] #右眼
    rex[2]=point[u'right_eye_lower_right_quarter'][u'x']
    rex[3]=point[u'right_eye_bottom'][u'x']
    rex[4]=point[u'right_eye_lower_left_quarter'][u'x']
    rex[5]=point[u'right_eye_left_corner'][u'x']
    rex[6]=point[u'right_eye_upper_left_quarter'][u'x']
    rex[7]=point[u'right_eye_top'][u'x']
    rex[8]=point[u'right_eye_upper_right_quarter'][u'x']
    rex[9]=point[u'right_eye_center'][u'x']
    rex[10]=point[u'right_eye_pupil'][u'x']
    
    rey[1]=point[u'right_eye_right_corner'][u'y']
    rey[2]=point[u'right_eye_lower_right_quarter'][u'y']
    rey[3]=point[u'right_eye_bottom'][u'y'] 
    rey[4]=point[u'right_eye_lower_left_quarter'][u'y']
    rey[5]=point[u'right_eye_left_corner'][u'y']   
    rey[6]=point[u'right_eye_upper_left_quarter'][u'y']
    rey[7]=point[u'right_eye_top'][u'y']   
    rey[8]=point[u'right_eye_upper_right_quarter'][u'y']     
    rey[9]=point[u'right_eye_center'][u'y']
    rey[10]=point[u'right_eye_pupil'][u'y']
      
    lbx[1]=point[u'left_eyebrow_left_corner'][u'x'] #左眉
    lbx[2]=point[u'left_eyebrow_lower_left_quarter'][u'x']
    lbx[3]=point[u'left_eyebrow_lower_middle'][u'x']
    lbx[4]=point[u'left_eyebrow_lower_right_quarter'][u'x']
    lbx[5]=point[u'left_eyebrow_right_corner'][u'x']
    lbx[6]=point[u'left_eyebrow_upper_right_quarter'][u'x']
    lbx[7]=point[u'left_eyebrow_upper_middle'][u'x']
    lbx[8]=point[u'left_eyebrow_upper_left_quarter'][u'x']
    
    lby[1]=point[u'left_eyebrow_left_corner'][u'y'] 
    lby[2]=point[u'left_eyebrow_lower_left_quarter'][u'y']
    lby[3]=point[u'left_eyebrow_lower_middle'][u'y']
    lby[4]=point[u'left_eyebrow_lower_right_quarter'][u'y']
    lby[5]=point[u'left_eyebrow_right_corner'][u'y']
    lby[6]=point[u'left_eyebrow_upper_right_quarter'][u'y']
    lby[7]=point[u'left_eyebrow_upper_middle'][u'y']
    lby[8]=point[u'left_eyebrow_upper_left_quarter'][u'y']
    
    rbx[1]=point[u'right_eyebrow_right_corner'][u'x'] #右眉
    rbx[2]=point[u'right_eyebrow_lower_right_quarter'][u'x']
    rbx[3]=point[u'right_eyebrow_lower_middle'][u'x']
    rbx[4]=point[u'right_eyebrow_lower_left_quarter'][u'x']
    rbx[5]=point[u'right_eyebrow_left_corner'][u'x'] 
    rbx[6]=point[u'right_eyebrow_upper_left_quarter'][u'x']
    rbx[7]=point[u'right_eyebrow_upper_middle'][u'x']
    rbx[8]=point[u'right_eyebrow_upper_right_quarter'][u'x']
    
    rby[1]=point[u'right_eyebrow_right_corner'][u'y']
    rby[2]=point[u'right_eyebrow_lower_right_quarter'][u'y']
    rby[3]=point[u'right_eyebrow_lower_middle'][u'y']
    rby[4]=point[u'right_eyebrow_lower_left_quarter'][u'y']
    rby[5]=point[u'right_eyebrow_left_corner'][u'y'] 
    rby[6]=point[u'right_eyebrow_upper_left_quarter'][u'y']
    rby[7]=point[u'right_eyebrow_upper_middle'][u'y']
    rby[8]=point[u'right_eyebrow_upper_right_quarter'][u'y']
    
    
    #绘制关键点
    '''
    cv2.circle(frame,(cx,cy),1,(0,255,0),-1)
    for j in range (9):
        cv2.circle(frame,(lx[j+1],ly[j+1]),1,(0,255,0),-1)
        cv2.circle(frame,(rx[j+1],ry[j+1]),1,(0,255,0),-1)
    for j in range (9):    
        cv2.circle(frame,(dmx[j+1],dmy[j+1]),1,(0,255,0),-1)
        cv2.circle(frame,(umx[j+1],umy[j+1]),1,(0,255,0),-1)
    for j in range (10):    
        cv2.circle(frame,(nx[j+1],ny[j+1]),1,(0,255,0),-1)
    for j in range (10):    
        cv2.circle(frame,(lex[j+1],ley[j+1]),1,(0,255,0),-1)
    for j in range (10):    
        cv2.circle(frame,(rex[j+1],rey[j+1]),1,(0,255,0),-1)
    for j in range (8):    
        cv2.circle(frame,(lbx[j+1],lby[j+1]),1,(0,255,0),-1)
    for j in range (8):    
        cv2.circle(frame,(rbx[j+1],rby[j+1]),1,(0,255,0),-1)
    '''
    '''
    cv2.circle(frame,(cx,cy),1,(255,0,0),-1)
    for j in range (9):
        cv2.circle(frame,(lx[j+1],ly[j+1]),1,(255,0,0),-1)
        cv2.circle(frame,(rx[j+1],ry[j+1]),1,(255,0,0),-1)
    for j in range (9):    
        cv2.circle(frame,(dmx[j+1],dmy[j+1]),1,(255,0,0),-1)
        cv2.circle(frame,(umx[j+1],umy[j+1]),1,(255,0,0),-1)
    for j in range (10):    
        cv2.circle(frame,(nx[j+1],ny[j+1]),1,(255,0,0),-1)
    for j in range (10):    
        cv2.circle(frame,(lex[j+1],ley[j+1]),1,(255,0,0),-1)
    for j in range (10):    
        cv2.circle(frame,(rex[j+1],rey[j+1]),1,(255,0,0),-1)
    for j in range (8):    
        cv2.circle(frame,(lbx[j+1],lby[j+1]),1,(255,0,0),-1)
    for j in range (8):    
        cv2.circle(frame,(rbx[j+1],rby[j+1]),1,(255,0,0),-1)
    '''
    #连线   
    '''
    for j in range (8):
        cv2.line(frame,(lx[j+1],ly[j+1]),(lx[j+2],ly[j+2]),(255,0,0),1)  
        cv2.line(frame,(rx[j+1],ry[j+1]),(rx[j+2],ry[j+2]),(255,0,0),1)  
        cv2.line(frame,(nx[j+1],ny[j+1]),(nx[j+2],ny[j+2]),(255,0,0),1)  
        
    cv2.line(frame,(lx[9],ly[9]),(cx,cy),(255,0,0),1)  
    cv2.line(frame,(rx[9],ry[9]),(cx,cy),(255,0,0),1)  
    
    for j in range (7):
        cv2.line(frame,(lex[j+1],ley[j+1]),(lex[j+2],ley[j+2]),(255,0,0),1)  
        cv2.line(frame,(rex[j+1],rey[j+1]),(rex[j+2],rey[j+2]),(255,0,0),1)  
        cv2.line(frame,(lbx[j+1],lby[j+1]),(lbx[j+2],lby[j+2]),(255,0,0),1)  
        cv2.line(frame,(rbx[j+1],rby[j+1]),(rbx[j+2],rby[j+2]),(255,0,0),1)  
        
    cv2.line(frame,(lex[1],ley[1]),(lex[8],ley[8]),(255,0,0),1)  
    cv2.line(frame,(rex[1],rey[1]),(rex[8],rey[8]),(255,0,0),1)  
    cv2.line(frame,(lbx[1],lby[1]),(lbx[8],lby[8]),(255,0,0),1)  
    cv2.line(frame,(rbx[1],rby[1]),(rbx[8],rby[8]),(255,0,0),1)  
    
    for j in range (8):
        cv2.line(frame,(dmx[j+1],dmy[j+1]),(dmx[j+2],dmy[j+2]),(255,0,0),1)  
        cv2.line(frame,(umx[j+1],umy[j+1]),(umx[j+2],umy[j+2]),(255,0,0),1)  
    
    cv2.line(frame,(dmx[1],dmy[1]),(umx[4],umy[4]),(255,0,0),1)  
    cv2.line(frame,(dmx[9],dmy[9]),(umx[4],umy[4]),(255,0,0),1)  
    cv2.line(frame,(dmx[6],dmy[6]),(umx[1],umy[1]),(255,0,0),1)  
    cv2.line(frame,(dmx[6],dmy[6]),(umx[9],umy[9]),(255,0,0),1)  
    '''
    for j in range (8):
        cv2.line(frame,(lx[j+1],ly[j+1]),(lx[j+2],ly[j+2]),(255,0,0),2)  
        cv2.line(frame,(rx[j+1],ry[j+1]),(rx[j+2],ry[j+2]),(255,0,0),2)  
        cv2.line(frame,(nx[j+1],ny[j+1]),(nx[j+2],ny[j+2]),(255,0,0),2)  
        
    cv2.line(frame,(lx[9],ly[9]),(cx,cy),(255,0,0),2)  
    cv2.line(frame,(rx[9],ry[9]),(cx,cy),(255,0,0),2)  
    
    for j in range (7):
        cv2.line(frame,(lex[j+1],ley[j+1]),(lex[j+2],ley[j+2]),(255,0,0),2)  
        cv2.line(frame,(rex[j+1],rey[j+1]),(rex[j+2],rey[j+2]),(255,0,0),2)  
        cv2.line(frame,(lbx[j+1],lby[j+1]),(lbx[j+2],lby[j+2]),(255,0,0),2)  
        cv2.line(frame,(rbx[j+1],rby[j+1]),(rbx[j+2],rby[j+2]),(255,0,0),2)  
        
    cv2.line(frame,(lex[1],ley[1]),(lex[8],ley[8]),(255,0,0),2)  
    cv2.line(frame,(rex[1],rey[1]),(rex[8],rey[8]),(255,0,0),2)  
    cv2.line(frame,(lbx[1],lby[1]),(lbx[8],lby[8]),(255,0,0),2)  
    cv2.line(frame,(rbx[1],rby[1]),(rbx[8],rby[8]),(255,0,0),2)  
    
    for j in range (8):
        cv2.line(frame,(dmx[j+1],dmy[j+1]),(dmx[j+2],dmy[j+2]),(255,0,0),2)  
        cv2.line(frame,(umx[j+1],umy[j+1]),(umx[j+2],umy[j+2]),(255,0,0),2)  
    
    cv2.line(frame,(dmx[1],dmy[1]),(umx[4],umy[4]),(255,0,0),2)  
    cv2.line(frame,(dmx[9],dmy[9]),(umx[4],umy[4]),(255,0,0),2)  
    cv2.line(frame,(dmx[6],dmy[6]),(umx[1],umy[1]),(255,0,0),2)  
    cv2.line(frame,(dmx[6],dmy[6]),(umx[9],umy[9]),(255,0,0),2)  
    
cv2.namedWindow("faceDetecion",0)
cv2.imwrite("line_"+filename2,frame) 
cv2.imshow("faceDetecion", frame)          
c = cv2.waitKey(0)     
cv2.destroyAllWindows()  

