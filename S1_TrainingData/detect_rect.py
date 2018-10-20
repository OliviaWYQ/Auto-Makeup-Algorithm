import requests  
from json import JSONDecoder  
import cv2  
import os  
import io, json
from glob import glob

def findrect(filename):
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"  
    key =""
    secret =""  
    fpath = 'E:\\MyProject\\S1_TrainingData_done\\S2_FindFace'
    
    name = os.path.split(filename)[1]
    data = {"api_key":key, "api_secret":secret, "return_landmark":"1"}  
    files = {"image_file":open(filename, "rb")}  
    response = requests.post(http_url, data=data, files=files)  
    req_con = response.content.decode('utf-8')  
    req_dict = JSONDecoder().decode(req_con)    
    #print (req_dict)
    
    with io.open(fpath+'\\'+'data.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(req_dict, ensure_ascii=False))    
    os.rename(fpath+'\\'+'data.txt',fpath+'\\'+name+'.json')

def cutrect(filename):
    name = os.path.split(filename)[1]
    fpath = 'E:\\MyProject\\S1_TrainingData_done\\S2_FindFace'+'\\'+name
    savepath='E:\\MyProject\\S1_TrainingData_done\\S2_FindFace'
    with open(fpath+".json",'r') as load_f:
        req_dict = json.load(load_f)
    face_num = len(req_dict[u'faces'])  
    #print (name)
    frame = cv2.imread(filename)  
    #cv2.imshow("frame", frame)
    #cv2.waitKey(0)
    for i in range(face_num):  
        box = req_dict[u'faces'][i][u'face_rectangle']  
        x, y, w, h = box[u'left'], box[u'top'],box[u'width'],box[u'height']  
        if (y-40<0):
            lefty = 0
        else: lefty = y-40
        if (x-25<0):
            leftx = 0
        else: leftx = x-25
        righty = y+h+10
        rightx = x+w+25
        face = frame[lefty:righty, leftx:rightx]     
        #print (lefty, righty, leftx, rightx)
        face = cv2.resize(face, (256, 256))
        save_filename = '%s_%d.jpg' % (os.path.basename(filename).split('.')[0], i)
        cv2.imwrite(savepath+'\\'+ save_filename, face)   
            
if __name__ == '__main__':
    '''
    file_list = glob('E:\MyProject\S1_TrainingData_done\S2_FindFace\western_B\*.jpg')
    for filename in file_list:
        #findrect(filename)
        cutrect(filename)
    '''
    filename = 'E:\\MyProject\\S1_TrainingData_done\\S2_FindFace'  
    filename2 = 'unify.jpg'
    filepath = os.path.join(filename, filename2)
    #findrect(filepath)
    cutrect(filepath)
   
