# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 22:37:05 2022

@author: Yasin
"""

from oop import Tavuk, TavukKumesi, Kedi

tavuk_kumesi1 = TavukKumesi()
tavuk1 = Tavuk("düz", 1, 5)
tavuk2 = Tavuk("yassı", 3, 7)
kedi1 = Kedi("hilal", 1, 5)

tavuk_kumesi1.tavuk_ekle(tavuk1)
tavuk_kumesi1.tavuk_ekle(tavuk2)
tavuk_kumesi1.tavuk_ekle(kedi1)


for tavuk in tavuk_kumesi1.get_tavuklar():
    print(tavuk.get_yas(), tavuk.get_gaga())


"""hayvan1 = Hayvan(3,15,4)
hayvan1.yaslan()
hayvan1.yaslan()
hayvan1.yaslan()
print("hayvanın ayak sayısı:", hayvan1.leg)
print("hayvanın yaşı:", hayvan1.get_yas())"""
