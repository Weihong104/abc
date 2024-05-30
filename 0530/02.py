# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:07:52 2024

@author: USER
"""

data=[10,20,30]
try:
    print(10/0)
    print(data[0])
    print(data[10])
    print(data[2])
except (IndexError,ZeroDivisionError) as err:
    #哪個錯誤先發生就會先顯示那個錯誤
    print(err)