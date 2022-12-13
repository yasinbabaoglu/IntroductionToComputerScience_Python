# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 20:03:34 2022

@author: talha
"""


class Node:
    def __init__(self, sayi=None, next=None):
        self.sayi = sayi
        self.next = next
        
        
class LinkedList:
    def __init__(self, head):
        self.head = head        

    def display(self):        
        current = self.head
        print(current.sayi, end=("-"))
        while not current.next is None:
            current = current.next
            print(current.sayi, end=("-"))
        print("")

    def push(self, num):
        current = self.head
        while not current.next is None:
            current = current.next
        current.next = Node(num)
        


class CustomList(LinkedList):
    def __init__(self, head):
        LinkedList.__init__(self, head)
            
    def getIndex(self,index):
        current = self.head
        i=0
        while not current.next is None and i < index:
            current = current.next
            i+=1
        if i == index:
           return current.sayi
        return None

    def updateIndex(self,index,num):
        current = self.head
        i=0
        while not current.next is None and i < index:
            current = current.next
            i+=1
        if i == index:
            current.sayi = num
        else:
            raise(Exception("indexe ulaşılamadı."))
 
    def pushIndex(self,index,num):
        current = self.head
        i=0
        while not current.next is None and i < index:
            current = current.next
            i+=1
        temp = current.next
        current.next = Node(num,temp)
        
    def popIndex(self,index):
        current = self.head
        i=0
        while not current.next.next is None and i < index-1:
            current = current.next
            i+=1
        temp = current.next
        current.next = current.next.next
        del temp


class Stack(LinkedList):
    def __init__(self, head):
        LinkedList.__init__(self, head)
    
    def popStack(self):
        current = self.head
        while not current.next.next is None:
            current = current.next
        del current.next
        current.next = None
    
    
class Queue(LinkedList):
    def __init__(self, head):
        LinkedList.__init__(self, head)
        
    def popQueue(self):
        temp = self.head
        self.head = self.head.next
        del temp

      
def append(linked_list, N):
    for i in range(1,N):
        linked_list.push(i)
        
        
head_ll = Node(0)
head_cl = Node(0)
head_stack = Node(0)
head_queue = Node(0)

linked_list = LinkedList(head_ll)
custom_list = CustomList(head_cl)
stack = Stack(head_stack)
queue = Queue(head_queue)
queue2 = Queue(Node(0))

#head.push(1)
#head.display()

append(linked_list, 20)
append(custom_list, 20)
append(stack, 20)
append(queue, 20)
append(queue2, 5)

print("Linked List:")
linked_list.display()

print("\nCustom List:")
custom_list.display()
custom_list.popIndex(3)
print(custom_list.getIndex(5))
custom_list.pushIndex(19, 20)
custom_list.updateIndex(18, 31)
custom_list.display()

print("\nStack:")
stack.display()
stack.popStack()
stack.popStack()
stack.push(97)
stack.display()

print("\nQueue:")
queue.display()
queue.popQueue()
queue.popQueue()
queue.push(54)
queue.display()

print("\nQueue2:")
queue2.display()
queue2.popQueue()
queue2.popQueue()
queue2.push(54)
queue2.display()



