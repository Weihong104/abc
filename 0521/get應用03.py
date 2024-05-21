# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:04:43 2024

@author: USER
"""

fruits={'apple':100,'banana':49,'orange':69}
print(fruits['orange'])
#print(fruits['cherray'])
print(fruits.get('cherray'))#用get顯示None
print(fruits)
print(fruits.get('cherray',10))#加上,可給值
print(fruits.get('cherray','找不到'))
print(fruits.get('banana','找不到'))#如果有值就無法給予

