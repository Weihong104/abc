# -*- coding: utf-8 -*-
"""

"""
class Father:
    def company(self):
        print('老爸公司:輝達')
    def showMoney(self):
        print('有三兆台幣')
    
class Son(Father):
    pass
class Daughter(Father):
    def company(self):
        print('在超微工作')
    def boyfriend(self):
        print('在intel服務')

son=Son()
daughter=Daughter()

son.company()
son.showMoney()
daughter.company()
daughter.showMoney()