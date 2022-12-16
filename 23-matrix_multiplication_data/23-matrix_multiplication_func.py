# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:11:42 2022

@author: Yasin
"""

def read_meta(file):
    text = file.readline().replace("\n", "")
    matrix1 = text.split(",")
    M, N = int(matrix1[0]),int(matrix1[1])
    return M, N

def read_matrix(size, file):
    matrix_list = []
    for i in range(size):
        temp = []
        text = file.readline().replace("\n", "")
        matrix2 = text.split(",")
        for j in matrix2:
            temp.append(int(j))
        matrix_list.append(temp)
    return matrix_list

path_input = "data/23.txt"
path_output = "data/23_result.txt"

file_input = open(path_input, "r")

M1, N1 = read_meta(file_input)
M2, N2 = read_meta(file=file_input)

if N1 == M2:
    c = []
    
    file_input.readline()
    a = read_matrix(M1, file_input)
    file_input.readline()
    b = read_matrix(M2,file_input)
    
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