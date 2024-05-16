# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:06:31 2024

@author: USER
"""

x=10
y=x
score=[99,66,72]

other=[99,66,72]
if x==y:
    print('兩者相同')
if score==other:
    print('兩者相同')

if x is y:             #is比較雙方的記憶體位置
    print('xy相同')
if score is other:
    print('串列相同')