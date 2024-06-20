# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:39:49 2024

@author: USER
"""

import csv

fn='test.csv'
date=[['A'],['B'],['C']]

with open (fn,'w',encoding='utf-8',newline='') as fObj:
    csvWriter=csv.writer(fObj)
    csvWriter.writerows(date)
    
           