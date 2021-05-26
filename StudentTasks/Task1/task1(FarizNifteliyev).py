# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:09:44 2021

@author: harry
"""

name = input('Adınızı Daxil Edin:')
surname = input('Soyadınızı Daxil Edin:')
age = int(input('Yaşınızı Daxil Edin:'))
counter_name = 0
counter_surname = 0
for i in name:
    counter_name += 1
for j in surname:
    counter_surname += 1
multi = age * (counter_name + counter_surname)
print(multi)
