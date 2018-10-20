import requests  
from json import JSONDecoder  
import io, json
import cv2  
import os  
import sys
import time

http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
#try
#key =""
#secret =""
#payed
key =""
secret =""
  
path = 'E:\\MyProject\\S4_ImageCutting_delay\\image\\face_rect_before2after_new\\FACE_western_A_new' 
files= os.listdir(path)
for file in files: 
    
    filename = os.path.split(file)[1]
    filepath = path+'\\'+filename
    data = {"api_key":key, "api_secret":secret, "return_landmark":"2"}  #2:106
    files = {"image_file":open(filepath, "rb")}  
    response = requests.post(http_url, data=data, files=files)  
    req_con = response.content.decode('utf-8')  
    req_dict = JSONDecoder().decode(req_con)  
    #print (req_dict)

    with io.open('data.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(req_dict, ensure_ascii=False))    
        
    os.rename('data.txt',filename+'.json')
