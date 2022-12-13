# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:29:38 2022

@author: Yasin
"""

N= int(input("Bir sayı girin: "))
a = []

for i in range(N):
    a.append(int(input(f"{i}. sayıyı gir: ")))

min=a[0]

for i in range(N):
    if min > a[i]:
        min = a[i]
print("Minimum sayı= ",min)
    
    