# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:49:34 2024

@author: USER
"""

class Father:
    def __init__(self,name,money):
        self.name=name
        self.money=money
        
    def __str__(self):
        print(self.name,self.money)
        return '__str__'
    def __repr__(self):
        msg='姓名:{}金額:{}'.format(self.name,self.money)
        return msg
    
f=Father('John', 1000000)
print(f)
print(repr(f))
   