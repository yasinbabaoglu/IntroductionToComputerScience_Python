# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:30:53 2022

@author: Yasin
"""

A = int(input("Bir sayı girin: "))
flag = True

for i in range(2,A,1):
    if A % i == 0:
        flag = False

if flag == True:
    print("Asal sayıdır.")
else:
    print("Asal sayı değildir.")
    

