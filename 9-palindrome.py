# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:12:23 2022

@author: Yasin
"""

A = int(input("3 basamaklı bir sayı gir: "))

birler = A % 10
yuzler = A / 100
yuzler = int(yuzler)

if yuzler == birler:
    print("Palendrom")
    
else:
    print("Palendrom değil")