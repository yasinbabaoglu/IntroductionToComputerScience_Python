# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:04:48 2022

@author: Yasin
"""

import math

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

        
def insert(key,node):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(key, node.left)
    else:
        node.right = insert(key,node.right)

    return node
    
def display(current):
    if not current is None:
        display(current.left)
        print(current.key)
        display(current.right)
            
            
        
root = Node(31)
insert(25, root)
insert(15, root)
insert(10, root)
insert(35, root)
insert(40, root)
insert(50, root)
insert(60, root)
insert(5, root)

display(root)

