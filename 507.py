# -*- coding: utf-8 -*-
"""

"""

msg='姓名:{}年齡:{}'.format('bill', 19)

print(msg)
msg='姓名:{0}利率:{1},別名:{0}'.format('連城',3.14)
print(msg) 

msg='現金{:,}元'.format(100000)
print(msg)
msg='姓名:{:10s}利率:{:2f}'.format('bill', 3.1415926)
print(msg)

msg='姓名:{:^10s}利率:{:2f}'.format('bill', 3.1415926)
print(msg)

msg='姓名:{:>10s}利率:{:2f}'.format('bill', 3.1415926)
print(msg)
#作業巴斯卡三角形