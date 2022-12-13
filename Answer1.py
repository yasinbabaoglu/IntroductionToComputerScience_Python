x = int(input("x değerini girin: "))
N = int(input("N değerini girin: "))

sonuc = 0

for i in range(1, 2*N+2, 2):
    sum = 1
    fakt = 1
    
    for j in range(1, i+1):
        sum = sum * x
        fakt = fakt * j
        
    if i % 4 == 1:
        sonuc += sum / fakt
    else:
        sonuc -= sum / fakt    
    
print(sonuc)