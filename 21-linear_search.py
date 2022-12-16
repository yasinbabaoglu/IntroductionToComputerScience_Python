# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:44:23 2022

@author: Yasin
"""

text1 = input("Birinci metni girin: \n")
text2 = input("İkinci metni girin: \n")

i = 0
flag = False

while flag == False and i < len(text1):
    j = 0
    flag = True
    
    while flag == True and j < len(text2):
        if i+j < len(text1):
            if not text1[i+j] == text2[j]:
                flag = False
           
        j += 1
    i += 1
    
if flag == True: 
    print(i)
else: 
    print("Yok.")
    
