# -*- coding: utf-8 -*-
import numpy as np
import math

def meanMethod(one,two):
    comb = zip(one,two)
    return [int(q/2+k/2) for q,k in comb]

def addMethod(one,two):
    comb = zip(one,two)
    return [int(q+k) for q,k in comb]

def divMethod(one,two):
    comb = zip(one,two)
    return [abs(q-k) for q,k in comb]

def maxMethod(one,two):
    comb = zip(one,two)
    return [max(q,k) for q,k in comb]

def minMethod(one,two):
    comb = zip(one,two)
    return [min(q,k) for q,k in comb]

def triMethod(one,two):
    comb = zip(one,two)
    return [int(2*q/3+k/3) for q,k in comb]

def addpoint(key):
    key[106] =  meanMethod(key[4],key[54])
    key[107] =  meanMethod(key[60],key[20])
    key[108] =  meanMethod(key[9],key[55])
    key[109] =  meanMethod(key[61],key[25])
    key[110] =  meanMethod(key[93],key[97])
    key[111] =  meanMethod(key[12],key[35])
    key[112] =  meanMethod(key[49],key[28])
    key[113] =  meanMethod(key[38],key[0])
    key[114] =  meanMethod(key[3],key[70])
    key[115] =  meanMethod(key[84],key[19])
    key[116] =  meanMethod(key[6],key[54])
    key[117] =  meanMethod(key[60],key[22])
    key[118] =  meanMethod(key[7],key[55])
    key[119] =  meanMethod(key[61],key[23])
    key[120] =  meanMethod(key[10],key[35])
    key[121] =  meanMethod(key[49],key[26])
    key[122] =  meanMethod(key[13],key[36])
    key[123] =  meanMethod(key[40],key[29])
    key[124] =  meanMethod(key[15],key[37])
    key[125] =  meanMethod(key[39],key[32])
    key[126] =  meanMethod(key[54],key[65])
    key[127] =  meanMethod(key[65],key[60])
    key[128] =  meanMethod(key[72],key[55])
    key[129] =  meanMethod(key[61],key[82])
    key[130] =  meanMethod(key[8],key[70])
    key[131] =  meanMethod(key[84],key[24])
    key[132] =   triMethod(key[7],key[35])
    key[133] =   triMethod(key[23],key[49])
    
def readData(name):
    with open(name, mode='r') as f:
        a = f.read()
        a1 = a.replace('\n',' ').replace('] [',' ').replace('[','').replace(']','')
        a2 = a1.split()
        a3 = list(map(int, a2))
        a4 = list(map(lambda b:a3[b:b+3],range(0,len(a3)-2,3)))
        #print (np.shape(a4))
        f.close()
    return a4

def printOriPoint(data4, data2, key11, key22, n): 
    '''
    for j in range (0, 8+20): 
        #data[(key1[j][0], key1[j][1])]= data2[(key2[j][0], key2[j][1])] 
        data4[(key11[j+106][0], key11[j+106][1])]= data2[(key22[j+106][0], key22[j+106][1])]        
        
        for k in range (0, 2*n):
            for q in range (0, 2*n):
                if key11[j+106][0]-n+q < 256 and key11[j+106][1]-n+k < 256 and key22[j+106][0]-n+q < 256 and key22[j+106][1]-n+k < 256:
                    #data[((key1[j][0]+q-10)%256, (key1[j][1]+k-10)%256)]= data2[((key2[j][0]+q-10)%256, (key2[j][1]+k-10)%256)]
                    data4[((key11[j+106][0]-n+q), (key11[j+106][1]-n+k))]= data2[((key22[j+106][0]-n+q), (key22[j+106][1]-n+k))]
    '''         
    for j in range (0, 106): 
        #data[(key1[j][0], key1[j][1])]= data2[(key2[j][0], key2[j][1])] 
        data4[(key11[j][0], key11[j][1])]= data2[(key22[j][0], key22[j][1])]        
        
        for k in range (0, 2*n):
            for q in range (0, 2*n):
                if key11[j][0]-n+q < 256 and key11[j][1]-n+k < 256 and key22[j][0]-n+q < 256 and key22[j][1]-n+k < 256:
                    #data[((key1[j][0]+q-10)%256, (key1[j][1]+k-10)%256)]= data2[((key2[j][0]+q-10)%256, (key2[j][1]+k-10)%256)]
                    data4[((key11[j][0]-n+q), (key11[j][1]-n+k))]= data2[((key22[j][0]-n+q), (key22[j][1]-n+k))]

def printTransPoint(data4, data2, key11, key22, n):     
    if key22[0][1]-key22[58][1] != 0:
        s = np.tanh((key22[0][0]-key22[58][0])/(key22[0][1]-key22[58][1]))
    else:
        s = 1
    s = abs(s)
    b = math.pi/2 - abs(s)
    h = int(np.sin(s)*2*n)
    w = int(np.cos(s)*2*n)

    for j in range (0, 28): 
    #data[(key1[j][0], key1[j][1])]= data2[(key2[j][0], key2[j][1])] 
        data4[(key11[j+106][0], key11[j+106][1])]= data2[(key22[j+106][0], key22[j+106][1])]        
        
        for k in range (0, 2*n):
            for p in range (0, 2*n):
                if k != 0:
                    x = np.tanh(p/k)
                else:
                    x = 1
                x = abs(x)
                m = math.pi/2 - abs(x)
                q = np.sqrt(np.power(p,2)+np.power(k,2))
                w1 = int(q * np.cos(s-m))
                h1 = int(q * np.sin(s-m))
              
                if key11[j+106][0]-n+p < 256 and key11[j+106][1]-n+k < 256 and key22[j+106][0]-n+h1 < 256 and key22[j+106][1]-n+w1 < 256:
                    #data[((key1[j][0]+q-10)%256, (key1[j][1]+k-10)%256)]= data2[((key2[j][0]+q-10)%256, (key2[j][1]+k-10)%256)]
                    data4[((key11[j+106][0]-n+p), (key11[j+106][1]-n+k))]= data2[((key22[j+106][0]-n+h1), (key22[j+106][1]-n+w1))]
        
    for j in range (0, 106): 
        #data[(key1[j][0], key1[j][1])]= data2[(key2[j][0], key2[j][1])] 
        data4[(key11[j][0], key11[j][1])]= data2[(key22[j][0], key22[j][1])]        
        
        for k in range (0, 2*n):
            for p in range (0, 2*n):
                if k != 0:
                    x = np.tanh(p/k)
                else:
                    x = 1
                x = abs(x)
                m = math.pi/2 - abs(x)
                q = np.sqrt(np.power(p,2)+np.power(k,2))
                w1 = int(q * np.cos(s-m))
                h1 = int(q * np.sin(s-m))
              
                if key11[j][0]-n+p < 256 and key11[j][1]-n+k < 256 and key22[j][0]-n+h1 < 256 and key22[j][1]-n+w1 < 256:
                    #data[((key1[j][0]+q-10)%256, (key1[j][1]+k-10)%256)]= data2[((key2[j][0]+q-10)%256, (key2[j][1]+k-10)%256)]
                    data4[((key11[j][0]-n+p), (key11[j][1]-n+k))]= data2[((key22[j][0]-n+h1), (key22[j][1]-n+w1))]
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    