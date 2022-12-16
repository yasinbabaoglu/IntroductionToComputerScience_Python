# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:48:33 2022

@author: Yasin
"""

#SELECTION SORT

N=int(input("Bir sayı girin: "))
a = []

for i in range(N):
    a.append(int(input(f"{i}. sayıyı gir: ")))

for i in range(N-1):
    for j in range(i+1, N):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
 
for i in range(N):
    print(a[i])
            
