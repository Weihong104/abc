# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:59:53 2024

@author: USER
"""

for i in range(2,101):
    for x in range(2,i):
        if i %x==0:
            print(i,'不是質數')
            break
    else:
        print(i,'是質數')