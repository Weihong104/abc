# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:47:08 2024

@author: USER
"""

class Father:
    def __init__(self,name):
        self.name=name
        self.money=0
    def display(self):
        print(self.name,self.money)

F=Father('Bill')

F.car='BMW'#可以在自己的子類做改變
print(F.car)

print(F.name)

a=Father('Tom')
print(a.name)
#   print(a.car)X