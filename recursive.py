# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 20:22:06 2022

@author: Yasin
"""

def fact(N):
    i = 1
    sum = 1
    while i <= N:
        sum = sum * i
        i+=1
    return sum

def fact_rec(N):
    if N == 1:
        return 1
    return N * fact_rec(N-1)

def us(x,n):
    if n == 0:
        return 1
    return x * us(x,n-1)
    
def fibonacci(n, f1=1, f2=1):
    if n == 1:
        return f1
    return fibonacci(n-1, f2, f1+f2)
    

N = 5
print(fact(N))
print(fact_rec(N))

x  = 2
n = 5
print(us(x,n))

fib_N = 7
print(fibonacci(fib_N))

