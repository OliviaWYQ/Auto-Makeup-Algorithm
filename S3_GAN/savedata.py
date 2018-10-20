# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import os

def img2data(image_path):
    
    file_queue = tf.train.string_input_producer([image_path]) #创建输入队列
    image_reader = tf.WholeFileReader()
    _, image = image_reader.read(file_queue)
    image = tf.image.decode_jpeg(image)

    with tf.Session() as sess:
    	coord = tf.train.Coordinator() #协同启动的线程
    	threads = tf.train.start_queue_runners(sess=sess, coord=coord) #启动线程运行队列
    	data = (sess.run(image))
    	coord.request_stop() #停止所有的线程
    	coord.join(threads)
        
    return data
    
if __name__ == '__main__':
    
    path = 'E:\\MyProject\\S5_GANPart\\tf04'
    #image = 'Amanda Seyfried_A_0.jpg'
    image = 'Alice Braga_B_1.jpg'
    image_path = os.path.join(path,image)
    data = img2data(image_path)
    
    #np.savetxt('data.txt', data, fmt='%s', newline='\n')
    np.savetxt('data2.txt', data, fmt='%s', newline='\n')
    #print (open("data2.txt").read())