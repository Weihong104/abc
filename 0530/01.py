# -*- coding: utf-8 -*-
"""
Created on Thu May 30 18:59:24 2024

@author: USER
"""
#data=[10,20,30]
#print(data[0])
#print(data[10])
#print(data[2])

data=[10,20,30]
try:
    print(data[0])
    print(data[10])
    print(data[2])
except IndexError:
    print('程式執行完畢')