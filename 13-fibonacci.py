# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:10:13 2022

@author: Yasin
"""

N= int(input("Bir sayı girin: "))

f1=1
f2=1
print(f1, f2, end=(" "))

for i in range(2,N+1,1):
    temp= f1
    f1= f2
    f2= f1 + temp
    print(f2, end=(" "))

print(len(str(f2)))
print("bitti")