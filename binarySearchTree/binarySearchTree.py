####
# Author: Nicholas Norman (NPN)
# Date: May 2024
# Last Modified:
#   NPN May 2024
# 
# A basic binary search tree
###

from node import *

class BinarySearchTree:
    
    #constr
    def __init__(self):
        #root of the tree is empty
        self.root:Node = None

    #setters and getters
    def getRoot(self):
        return self.root
    
    def setRoot(self, root:Node):
        self.root = root

    #search

    #insert
    def insert(self, value:int = 0):
        #insert this value into the tree
        
        #search for the values position
        if (self.root == None):
            #no root yet, this is my root
            self.root = Node(value)
        else:
            pass
            #create a node
            #add to R or L

    #delete