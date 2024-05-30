# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:47:03 2024

@author: USER
"""

try:
    result=10/2
    print(result)
except Exception as e:
    print(e)
finally:
    print('一定會執行')
print('Finish')