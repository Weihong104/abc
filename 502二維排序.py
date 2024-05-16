# -*- coding: utf-8 -*-
"""

"""
item=[[10,20,30],[1,2,3,4,5,6]]
       #1 2  3 
        #0              1     
print(item[0][2])

print(item[1])

print(len(item))

for data in item:       #用巢狀迴圈抓出裡面的值
    for i in data:
        print(i)
    print()