# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:11:21 2024

@author: USER
"""

n1=[10,20,30,40]

n2=[]

for i in n1:
    n2.append(i)

print(n1)
print(n2)

n1[0]=100
print(n2)

import copy
n3=copy.copy(n2)#淺複製 用於淺複製
print(n3)
n2[0]=699
print(n3)
print(n2)

d=[10,20,[1,2,3]]
e=copy.copy(d)

print(e)
d[2][0]=99
print(d)
print(e)
f=copy.deepcopy(d)
d[2][1]=699
print(d)
print(f)