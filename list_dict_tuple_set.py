# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 21:10:47 2022

@author: Yasin
"""

yok = None
if yok is None:
    print("yok: None")

a = list() 
a = [1,-9,8]
if -9 in a:
    print("-9 var")

b = dict() # b["yasin"] b.get("yasin")
b = {"yasin":25, "talha": 24} 
b["yasar"] = 23
b["yasin"] = 26
print(b)
# print(b["afy"])
print(f'afy: {b.get("afy")}, yasin: {b.get("yasin")}')
if b.get("afy") is None:
    print("afy: None")

c = tuple() 
c = ((1,5),(2,-9))
print(f"c[1]: {c[1]}, c[1][1]: {c[1][1]}")

d = set()

    