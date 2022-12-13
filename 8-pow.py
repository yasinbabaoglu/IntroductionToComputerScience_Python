# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:49:44 2022

@author: Yasin
"""

a= float(input("Bir sayı gir: "))
b= int(input("Üssünü gir: "))

sum=1
if b < 0:
    a = 1 / a
    b = -b
"""
for i in range(b):
    sum=sum*a  
"""

i=1
while(i < b+1):
    sum=sum*a
    i=i+1
    
print(int(sum))
    