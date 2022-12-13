# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:52:27 2022

@author: Yasin
"""

text = input("Metin gir: ")

for i in range(len(text)):
    if text[i] == '.' and text[i+1] >= 'a' and text[i+1] <= 'z':
        #text = text[:i+1] + text[i+1].upper() + text[i+2:] # - (chr('a') - chr('A'))
        text = text.replace("."+text[i+1], "."+text[i+1].upper())
        #text[i+1] = chr(ord(text[i+1]) - (ord('a') - ord('A')))
        
print(text)
    