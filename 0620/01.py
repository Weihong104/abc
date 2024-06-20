# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:30:12 2024

@author: USER
"""

import csv
fn='member.csv'
with open(fn,encoding='utf-8') as fObj:
    csvDic=csv.DictReader(fObj)
    for row in csvDic:
        print(row)
        for item in row:
            print(row['name'])