# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:07:03 2024

@author: USER
"""
class Father:
    def play(self, item):
        print('使用', item, '來玩')

class Son:
    def go(self):
        print('bike')
        
son = Son()  # 創建了一個Son類的實例

son.go()  # 調用Son類的go方法

Father.play(son, '球棒')  
# 調用Father類的play方法，傳遞Son類的實例和球棒參數





