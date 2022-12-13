# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:53:27 2022

@author: Yasin
"""

N = int(input("Bir sayı girin: "))
sum = 1

for i in range(1,N+1):
    sum = sum*i
    
print(sum)