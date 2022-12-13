# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 20:03:34 2022

@author: talha
"""


class Node:
    def __init__(self, sayi=None, next=None):
        self.sayi = sayi
        self.next = next
    
    def push(self,num):
        current = self
        while not current.next is None:
            current = current.next
        current.next = Node(num)

    def display(self):        
        current = self
        print(current.sayi, end=("-"))
        while not current.next is None:
            current = current.next
            print(current.sayi, end=("-"))
        print("")
        
    def pop(self):
        current = self
        while not current.next.next is None:
            current = current.next
        del current.next
        current.next = None
    
    def getIndex(self,index):
        current = self
        i=0
        while not current.next is None and i < index:
            current = current.next
            i+=1
        if i == index:
           return current.sayi
        return None
        
    def pushIndex(self,index,num):
        current = self
        i=0
        while not current.next is None and i < index:
            current = current.next
            i+=1
        temp = current.next
        current.next = Node(num,temp)
        
    def popIndex(self,index):
        current = self
        i=0
        while not current.next.next is None and i < index-1:
            current = current.next
            i+=1
        temp = current.next
        current.next = current.next.next
        del temp
    
    def updateIndex(self,index,num):
        current = self
        i=0
        while not current.next is None and i < index:
            current = current.next
            i+=1
        if i == index:
            current.sayi = num
        else:
            raise(Exception("indexe ulaşılamadı."))
            
def append(head, N):
    for i in range(1,N):
        head.push(i)
        
        
head = Node(0)

#head.push(1)
#head.display()

append(head, 20)
head.pop()
head.display()

print(head.getIndex(5), head.getIndex(25))

head.pushIndex(5, 31)
head.display()

head.popIndex(10)
head.display()

head.updateIndex(45,32)
head.display()


