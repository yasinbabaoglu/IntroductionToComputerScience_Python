# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:01:15 2022

@author: Yasin
"""

a= int(input("a sayısını gir: "))
b= int(input("b sayısını gir: "))

temp= a
a = b
b = temp

print("a=", a)
print("b=", b)