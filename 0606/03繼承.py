# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:34:49 2024

@author: USER
"""

class Father:
    def car(self):
        print('Father car:BMW')
    def house(self):
        print('Father:七期')

class Mother:
    def car(self):
        print('Mother car:保時捷')
    def land(self):
        print('Mother土地在14期')
    
    
class Son(Father,Mother):
    pass


son=Son()
son.car()
son.house()
son.land()
