# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:30:28 2018

@author: Administrator
"""

import win_unicode_console
win_unicode_console.enable()

from PIL import Image
import os
import numpy as np
import random

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.utils import to_categorical
from keras import regularizers

x_train = []
x_target = []

y_test = []
y_target = []

#s11_01
n=0
path=r".\Face Database ori"
#print(os.listdir(path))

for filename in os.listdir(path):
    if(filename[0] == 's'):
        test = Image.open(path+'\\'+filename)
        
        num = int(filename[1]) * 10 + int(filename[2]) 
        matrix = np.array(test) / 255
        num_temp = int(filename[4]) * 10 + int(filename[5]) 
        #print(matrix[0][0])

        
        if(n!=num):
            n=num
            random_list=[1,2,3,4,6,7,8,10,11,12,13,14,15]
            random.shuffle(random_list)
        if(num_temp==random_list[0] or num_temp==random_list[1]):
            y_test.append(matrix)
            y_target.append(num)
        else:
            x_train.append(matrix)
            x_target.append(num)
            



        
  
x_data = np.array(x_train)
x_label = np.array(x_target)          

y_data = np.array(y_test)
y_label = np.array(y_target)

print(x_data.shape)
print(y_data.shape)

x_label = to_categorical(x_label,num_classes = 51)
y_label = to_categorical(y_label,num_classes = 51)

model = Sequential()

model.add(Conv2D(64, 3, activation="relu", input_shape=(240, 180, 3),padding='valid'))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, 3 , activation="relu",padding='valid'))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))

"""
model.add(Dense(64, input_dim=64,
                kernel_regularizer=regularizers.l2(0.000001),
                activity_regularizer=regularizers.l1(0.000001)))
"""


model.add(Conv2D(32, 3, activation="relu",padding='valid'))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))

model.add(Dense(51, activation='softmax'))

model.summary()

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

train_history = model.fit(x_data,x_label,
          batch_size=16,
          epochs=20,
          verbose=1,
          shuffle=True,
          validation_data=(y_data,y_label))

model.save(r'.\model.h5')

score = model.evaluate(y_data,y_label,verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
