# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:41:03 2021

@author: Bilgi
"""

class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    def __str__(self):
        return str(self.info)
    
def preOrder(root):
    if root==None:
        return
    print(root.info, end = "")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        root = self.root
        while True:
            if val < root.info:
                if root.left is not None:
                    root =root.left
                else:
                    root.left = Node(val)
                    break
            elif val >=root.info:
                if root.right is not None:
                    root = root.right
                else:
                    root.right=Node(val)
                    break
    def traverse_inorder(self,root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.info)
            self.traverse_inorder(root.right)
            
    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1

tree = BinarySearchTree()

tree.insert(5)
root = tree.root
print(root)
tree.insert(4)   
tree.insert(2)   
tree.insert(7)   
tree.insert(1)   
tree.insert(3)  
    
print('---In traverse order---:')
tree.traverse_inorder(root)

print('==height====')
print(f'height of the tree is {tree.height(root)}')