# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:18:46 2022

@author: Yasin
"""

text = input("Bir metin gir:\n")

"""
a = []
for i in range(26):
    a.append(0)
    

for i in text:
    if i >= "a" and i <= "z":
        index = ord(i) - ord("a")
        a[index] +=1
"""

a = {}
#a = dict()

for i in range(26):
    a[chr(ord('a')+i)] = 0

for i in text:
    if i >= "a" and i <= "z":
        a[i] +=1

print(a)

"""
for key, value in a.items():
    print(f"{key}: {value}")
"""    
