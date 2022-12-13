# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:38:49 2022

@author: Yasin
"""

from math import sqrt

########## ASAL #################

N = int(input("Bir sayı girin: "))

for i in range(2,N,1):
    flag = True
    """
    for j in range(2,int(sqrt(i)+1),1):
        if i % j == 0:
            flag = False
    """
    j = 2
    while j <= int(sqrt(i)) and flag == True:
        if i % j == 0:
            flag = False
        j += 1 #j=j+1
    
    if flag == True:
        print(i,end=(","))
    
print("finish")    