# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:46:50 2022

@author: Yasin
"""

a = int(input("1. Sayıyı gir: "))
b = int(input("2. Sayıyı gir: "))

c = a / b
c = int(c)
if c % 2 == 0 and c > 10:
    c=c-5
    print("Sonuç:" , c)
else:
    print("Şartlar Sağlanmıyor")    
