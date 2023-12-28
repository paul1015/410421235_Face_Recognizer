# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:30:28 2018

@author: Administrator
"""

import win_unicode_console
win_unicode_console.enable()

from PIL import Image
from keras.models import load_model
import os
import numpy as np
import operator

model = load_model('model6.h5')
model.summary()

#path=r".\testData"
path=r".\Face Database ori"
error = 0
for filename in os.listdir(path):
    if(filename[0] == 's'):
        test = Image.open(path+'\\'+filename)
        Ans = int(filename[1]) * 10 + int(filename[2])
        temp = int(filename[4]) * 10 + int(filename[5])
        matrix = np.array(test) / 255
        matrix = matrix[np.newaxis,...]
        result = model.predict(matrix)
        #print(result.shape)
		
        result_dict = {}
        for i in range(len(result[0])):
            result_dict[i] = float(result[0][i])
        sorted_result_dict = sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True)

        print("\nPredict Ans:")
        print(sorted_result_dict[0][0])
        print("\ncurrect Ans:")
        print(Ans)

        print('\ntop-5 candidate: ')
        count = 0
        for topf in sorted_result_dict:
            count += 1
            print(str(topf[0])+' Possibility: %0.8f' %(topf[1]))
            if count >= 5:
                break

        
        if(sorted_result_dict[0][0]!=Ans):
            print(Ans,temp)
            #pause=input('\nUU')
            error += 1

print('error:' , error) 
            
