# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:30:28 2018

@author: Administrator
"""

from PIL import Image
import os



path = r"./Face Database"
#path = r"./testData"

for filename in os.listdir(path):
    if(filename[0] == 's'):
        test = Image.open(path+'\\'+filename)
        test = test.resize((180,240),Image.BILINEAR)
        test.save(path+'\\'+filename)

"""
def resize_image(image, height = IMAGE_SIZE, width = IMAGE_SIZE):

    h, w, _ = image.shape
    
    #最長的一邊
    longest_edge = max(h, w)    
    
    #哪邊要加
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass 
    
    #顏色RGB
    BLACK = [0, 0, 0]
    
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)
    
    return cv2.resize(constant, (height, width))
"""
