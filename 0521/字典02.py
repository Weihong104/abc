# -*- coding: utf-8 -*-
"""
字典
"""

score={'Math':61,'Eng':99,'Chi':82}
        #key:value
        #鍵:值 值可重複鍵不可重複
number={1:'Apple',10:'Banana'}

date=dict()
print(score['Math'])
print(number[10])

#改裡面的東西
score['Eng']=100
print(score)

score['Com']=72#如果沒有就會新增
print(score)