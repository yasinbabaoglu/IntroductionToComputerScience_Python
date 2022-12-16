# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:11:42 2022

@author: Yasin
"""

path_input = "data/23.txt"
path_output = "data/23_result.txt"

file_input = open(path_input, "r")

text = file_input.readline().replace("\n", "")
matrix1 = text.split(",")
M1, N1 = int(matrix1[0]),int(matrix1[1])

text = file_input.readline().replace("\n", "")
matrix2 = text.split(",")
M2, N2 = int(matrix2[0]),int(matrix2[1])

if N1 == M2:
    a = []
    b = []
    c = []
    file_input.readline()
    for i in range(M1):
        temp = []
        text = file_input.readline().replace("\n", "")
        matrix1 = text.split(",")
        for j in matrix1:
            temp.append(int(j))
        a.append(temp)
    file_input.readline()
    for i in range(M2):
        temp = []
        text = file_input.readline().replace("\n", "")
        matrix2 = text.split(",")
        for j in matrix2:
            temp.append(int(j))
        b.append(temp)
        
        
    for i in range(M1):
        temp = []
        for j in range(N2):
            sum = 0
            for k in range(N1):
                x = a[i][k] * b[k][j]     ###DANGER!!###
                sum = sum + x
            temp.append(sum)
        c.append(temp)
    
    file_output = open(path_output, "w")
    for satir in c:
        print(satir)
        file_output.write(str(satir) + "\n")
        """
        for sutun in satir:
            print(sutun,end=" ")
        print("")
        """
        
    file_output.close()

else:
    print("Yanlış")
    
file_input.close()