# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:14:43 2024

@author: USER
"""

data=[10,20,30]
try:
    print(10/0)
    print(data[0])
    print(data[10])
    print(data[2])
except Exception as err:
    #哪個錯誤先發生就會先顯示那個錯誤
    print(err)