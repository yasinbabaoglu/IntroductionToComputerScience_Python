# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:28:52 2022

@author: Yasin
"""

class Hayvan:
    def __init__(self,yas,kilo,leg):
        self._yas=yas
        self._kilo=kilo
        self.leg=leg
    
    def yaslan(self):
        self._yas=self._yas + 1
    
    def kilo_al(self,kilo):
        self._kilo=self._kilo+kilo
 
    def get_yas(self):
        return self._yas
    
class Kedi(Hayvan):
    def __init__(self,biyik,yas,kilo):
        Hayvan.__init__(self, yas, kilo, 4)
        self._biyik = biyik
    
    def set_biyik(self,biyik_type):
        self._biyik = biyik_type
        
    def get_biyik(self):
        return self._biyik
    
class Tavuk(Hayvan):
    def __init__(self,gaga,yas,kilo):
        Hayvan.__init__(self, yas, kilo, 2)
        self._gaga = gaga
    
    def set_gaga(self,gaga_type):
        self._gaga = gaga_type
    
    def get_gaga(self):
        return self._gaga
    
class TavukKumesi:
    def __init__(self):
        self._tavuklar = []
    
    def tavuk_ekle(self,tavuk):
        if type(tavuk) is Tavuk:
            self._tavuklar.append(tavuk)
        else:
            print("type yanlış:", type(tavuk))

    def get_tavuklar(self):
        return self._tavuklar


def multiple_yaslan(tavuk, yas=1):
    for i in range(yas):
        tavuk.yaslan()
    

if __name__ == "__main__": #main fonkiyon
        
    tavuk_kumesi1 = TavukKumesi()
    tavuk1 = Tavuk("düz", 1, 5)
    tavuk2 = Tavuk("yassı", 3, 7)
    kedi1 = Kedi("hilal", 1, 5)
    
    tavuk_kumesi1.tavuk_ekle(tavuk1)
    tavuk_kumesi1.tavuk_ekle(tavuk2)
    tavuk_kumesi1.tavuk_ekle(kedi1)
    
    multiple_yaslan(tavuk1, 10)

    tavuk4=tavuk1
    
    multiple_yaslan(tavuk4, 6)

    for tavuk in tavuk_kumesi1.get_tavuklar():
        print(tavuk.get_yas(), tavuk.get_gaga())
    
    """hayvan1 = Hayvan(3,15,4)
    hayvan1.yaslan()
    hayvan1.yaslan()
    hayvan1.yaslan()
    print("hayvanın ayak sayısı:", hayvan1.leg)
    print("hayvanın yaşı:", hayvan1.get_yas())"""
