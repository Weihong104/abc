# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Motor:  # 定義了一個名為Motor的類
    def __init__(self, name, price=95, capacity=1800):  
        # 定義了類的初始化方法，接受名稱、價格和容量三個參數
        self.name = name  
        # 將傳入的名稱參數賦值給實例的name屬性
        self.price = price  
        # 將傳入的價格參數賦值給實例的price屬性，如果沒有提供，默認為95
        self.capacity = capacity  
        # 將傳入的容量參數賦值給實例的capacity屬性，如果沒有提供，默認為1800
    
    def equip(self, award):  
        # 定義了一個名為equip的方法，接受獎勵參數
        self.price += award  
        # 將傳入的獎勵參數加到實例的價格屬性上
    
    def __str__(self):  
        # 定義了類的字串表示形式方法，該方法將實例轉換為字串
        msg = '{0:8s},售價:{1:7.2f}元,排氣量:{2:,}CC數'  
        # 格式化字串，用於描述實例的屬性
        return msg.format(self.name, self.price, self.capacity)  
        # 返回格式化後的字串
        
class Hybrid(Motor):  # 定義了一個名為Hybrid的子類，繼承自Motor類
    def equip(self, award, cell=3.64):  
        # 定義了equip方法，接受獎勵和電池參數，默認為3.64
        Motor.equip(self, award + cell)  
        # 呼叫了Motor類的equip方法並傳遞了修改後的獎勵值

    def tinted(self, color):  # 定義了tinted方法，接受一個顏色參數
        if color == 'r':  # 如果顏色是紅色
            return "大方紅"  # 返回大方紅
        else:  # 否則
            return '神秘黑'  # 返回神秘黑

m=Motor("stand")

print(m)

s=Motor('stand')

apollo=Motor('Apollo',price=81.2,capacity=1500)

print(apollo,'不含電子防盜鎖')

apollo.equip(1.9)
inno=Hybrid('Innovate',360.12)
inno.equip(1.3)

print('Hybrid color is',inno.tinted('r'))

print('三種車款')

for item in(s,apollo,inno):
    print(item)
