# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:38:08 2024

@author: USER
"""
        #軍師
class Advister:  
    def __init__(self,name,hp,mp):
        self.__name=name
        self.__hp=hp
        self.__mp=mp
    
    def fight(self):
        print('使用扇子攻擊')
    
    def cure(self):
        print('群體補血')
    
    def deathblow(self):
        print('火龍泡')
    
    def getName(self):
        return self.__name
    
    def getHP(self):
        return self.__hp
    
    def getMp(self):
        return self.__mp
    
    def setHp(self,hp):
        self.__hp=hp
    
    def setMp(self,mp):
        self.__mp=mp
        
        