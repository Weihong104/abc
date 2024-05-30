# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:59:41 2024

@author: USER
"""

def divfun(num1,num2):
    try:
        result=divmod(num1, num2)
    except:
        print('捕獲error')
    else:
        print(result)
    finally:
        print('計算完成')
divfun(1,0)
divfun(10,2)