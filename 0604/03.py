# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:18:03 2024

@author: USER
"""

class Pen(object):
    def setcolor(self,color):
        self.color=color

    def setName(self,name):
        self.name=name
    def display(self):
        print('顏色:',self.color)
        print('品牌:',self.name)
p=Pen()
p2=Pen()

p.setcolor('紅色')
p.setName('SDI')
p2.setcolor('藍色')
p2.setName('櫻花')
p.display()
p2.display()