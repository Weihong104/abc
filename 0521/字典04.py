# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:15:48 2024

@author: USER
"""

student={'john':81,'peter':62}
student['bill']=100
print(student)
student.update({'mary':83,'sue':98})
print(student)

print('排序')
for k in sorted(student):
    print('%-12s %3d'%(k,student[k]))
student.pop('john')

print(student)
for k in sorted(student,reverse=True):
    print('%-12s %3d'%(k,student[k]))
print('清空字典',student.clear())#清空

student.update(eric=92, george=73)
print(student)

