# -*- coding: utf-8 -*-
"""
count計算
index目標索引位置
"""

words=['a','b','c','d','a','c','f']
a=words.count('a')#計算
f=words.count('f')
g=words.count('g')
print('a有:',a)
print('f有:',f)
print('g有:',g)
ind=words.index('b')#b的索引位置
print(ind)
'''
ind=words.index('z')
print(ind)
如果目標沒有會發生錯誤
'''

start=0
for i in range(words.count('c')):
    #ind=words.index('c')如果有複數將會只抓第一個
    ind=words.index('c',start)
    print('c的索引:',ind)
    start = ind+1
    
    