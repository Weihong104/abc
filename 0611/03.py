# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:32:22 2024

@author: USER
"""

class Mother():
    def display(self, pay):
        self.price = pay  # 將傳入的支付參數賦值給實例的價格屬性

        if self.price >= 30000:  # 如果價格超過30000
            self.price *= 0.9  # 折扣9折
            
        print('={:,}'.format(self.price))  # 顯示最終價格
        
class Daughter(Mother):
    def display(self, pay):
        self.price = pay  # 將傳入的支付參數賦值給實例的價格屬性
        super().display(pay)  # 調用父類的display方法，傳遞支付參數
        if self.price >= 30000:  # 如果價格超過30000
            self.price *= 0.8  # 折扣8折
        print('8折{:,}'.format(self.price))

Mary=Mother()

print('40000打九折',end='')

Mary.display(40000)

Cherry =Daughter()

print('30000打九折',end='')

Cherry.display(30000)