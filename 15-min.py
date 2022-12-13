# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:05:38 2022

@author: Yasin
"""

N= int(input("Bir sayı girin: "))

min= int(input())

for i in range(1,N,1):
    a= int(input())
    if(min > a):
        min = a

print("Minimum sayı=", min)    