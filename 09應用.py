# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:07:17 2024

@author: USER
"""

print('學生成績系統')

students = []  # 建立一個空的學生列表

score = list()  # 建立一個空的成績列表

while True:
    q = input('請輸入姓名查成績(q離開):')  # 詢問使用者要查詢哪位學生的成績
    if q == 'q':
        break  # 如果使用者輸入了 'q'，則退出迴圈
    if students.count(q) == 1:  # 如果學生名單中已經有這個學生
        ind = students.index(q)  # 找到該學生在列表中的索引
        print('學生:', students[ind], '分數為:', score[ind])  # 印出該學生的成績
    else:
        ans = input('是否加入此學生(y\n)')  # 詢問是否要加入這位新學生
        if ans.lower() == 'y':
            s = int(input('輸入分數:'))  # 如果要加入，輸入該學生的成績
            students.append(q)  # 將學生姓名加入學生列表
            score.append(s)  # 將學生的成績加入成績列表

print(students)  # 印出所有學生的姓名列表
print(score)  # 印出所有學生的成績列表
