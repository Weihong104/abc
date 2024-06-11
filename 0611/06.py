# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:25:38 2024

@author: USER
"""

class Father:
    def display(self,name):
        self.name=name
        print('Father name is',self.name)

class Mother:
    def display(self,name):
        self.name=name
        print('Mother name is',self.name)



class Child(Father,Mother):
    pass

class Son(Father):
    pass

print(Child.__name__,'類別,繼承2個類別')

for item in Child.__bases__:
    print(item)
    
John=Son()
John.display('Tom')
print('Son的父類:',Son.__bases__)

Son.__bases__=(Mother,)
John.display('Mary')



