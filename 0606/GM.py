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

class Dancer:
    def __init__(self,name,hp,mp):
        self.__name=name
        self.__hp=hp
        self.__mp=mp
    
    def fight(self):
        print('使出回旋踢')
        
    def song(self):
        print('獅吼功')
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getMp(self):
        return self.__mp
    
    def setHp(self,hp):
        self.__hp=hp

    def setMp(self,mp):
        self.__mp=mp
        
class Saber:
    def __init__(self,name,hp,mp):
        self.__name=name
        self.__hp=hp
        self.__mp=mp

    def fight(self):
        print('揮砍')

    def Deathblow(self):
        print('誓約勝利之劍')

    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    def getMp(self):
        return self.__mp

    def setHp(self,hp):
        self.__hp=hp

    def setMp(self,mp):
        self.__mp=mp