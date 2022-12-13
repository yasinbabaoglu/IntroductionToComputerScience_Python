# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:03:07 2022

@author: Yasin
"""

a = input("metin gir: ")

count = 0

"""
for i in range(len(a)):
    if a[i] >= "A" and a[i] <= "Z":
        count += 1
"""

for i in a:
    if i >= "A" and i <= "Z":
        count += 1


print(count)



