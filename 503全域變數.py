# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:11:38 2024

@author: USER
"""

a=100
b=a
print(id(a)) # 將變數 a 的內存地址打印出來
print(id(b)) # 將變數 b 的內存地址打印出來
a=199
print(id(a)) # 改變變數 a 的值為 199，此時 a 將指向一個新的內存地址

item=[10,20,30,40]
data=item
print(id(item))
print(id(data))
item[0]=199 
# 改變變數 item 中的元素值，由於 data 和 item 指向同一個內存地址，
# 所以 data 的值也會隨之改變
print(data)
print(id(data))


