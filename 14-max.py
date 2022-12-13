# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:07:45 2022

@author: Yasin
"""

N= int(input("Bir sayı girin: "))

max= 0

for i in range(1,N+1,1):
    a= int(input())
    if(max < a):
        max = a

print("Maksimum sayı=", max)    
        
        
    