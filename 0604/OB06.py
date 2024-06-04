# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:17:59 2024

@author: USER
"""

class Account():
    def __init__(self,number,name,money):
        self.number=number
        self.name=name
        self.balance=money
    
    def deposite(self,money):
        if money>0:
            self.balance+=money
        
        else:
            raise RuntimeError('不可為頁')
    
    def withDraw(self,money):
        if self.balance>=money:
            self.balance-=money
    
    def showmoney(self):
        return self.balance
    
ac=Account('123-456-789', 'A', 1000)
ac2=Account('987-564-321', 'B', 30000)


ac.deposite(5000)
print(ac.showmoney())

ac2.deposite(-1000)
