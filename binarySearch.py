# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:51:38 2022

@author: Yasin
"""

import random
import time

def linearSearch(a, x):
    print("\nLinear Search:")
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binarySearch(a, x):
    print("\nBinary Search:")
    Li = 0
    Hi = len(a) - 1
    Mi = int((Hi+Li)/2)
    
    while (not a[Mi] == x) and (not Li == Hi):
        if x > a[Mi]:
            Li = Mi+1
        else:
            Hi = Mi -1
        Mi = int((Hi+Li)/2)
    if (a[Mi] == x):
        return Mi
    return -1
        

N = 90001
a = []
for i in range(N):
    a.append(random.randint(0, N))    
a.sort()
print(a)
x = int(input("X: "))

start =time.time()
print(linearSearch(a, x))
end =time.time()
print(end-start)

start =time.time()
print(binarySearch(a, x))
end =time.time()
print(end-start)

        
    