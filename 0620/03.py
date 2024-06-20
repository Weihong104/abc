# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:02:35 2024

@author: USER
"""

import csv
fn='student.csv'
with open(fn,'w',newline='',encoding='utf-8') as fObj:
    fields=['name','sex','tel']
    dictWriter=csv.DictWriter(fObj, fieldnames=fields)
    dictWriter.writeheader()
    dictWriter.writerow({'name':'王大德','sex':'男','tel':'0912666999'})
    dictWriter.writerow({'name':'葉大德','sex':'男','tel':'0912556999'})
