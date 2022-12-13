# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:25:36 2022

@author: Yasin
"""

M1 = int(input("1. matrisin satır sayısını girin: "))
N1 = int(input("1. matrisin sütun sayısını girin: "))
M2 = int(input("2. matrisin satır sayısını girin: "))
N2 = int(input("2. matrisin sütun sayısını girin: "))

if not N1 == M2:
    a = []
    b = []
    c = []
    
    for i in range(M1):
        temp = []
        for j in range(N1):
            temp.append(int(input(f"1. matris {i}. satır {j}. sütun değerini gir: ")))
        a.append(temp)

    for i in range(M2):
        temp = []
        for j in range(N2):
            temp.append(int(input(f"2. matris {i}. satır {j}. sütun değerini gir: ")))
        b.append(temp)
    
    for i in range(M1):
        temp = []
        for j in range(N2):
            sum = 0
            for k in range(N1):
                x = a[i][k] * b[k][j]
                sum = sum + x
            temp.append(sum)
        c.append(temp)
    
    for satir in c:
        print(satir)
        """
        for sutun in satir:
            print(sutun,end=" ")
        print("")
        """

else:
    print("Yanlış")