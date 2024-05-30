# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:27:38 2024

@author: USER
"""

def divfun(n1,n2):
    try:
        result=divmod(n1, n2)
        print(result)
    except Exception as e :
        print('fun處理')
        raise Exception(e)#將這個丟出去
try:
    divfun(10, 0)
except Exception as e:
    print('主程式')
    print(e)