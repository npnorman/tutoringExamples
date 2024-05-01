####
# Author: Nicholas Norman (NPN)
# Date: Apr 2024
# Last Modified:
#   NPN Apr 2024
# 
# A basic node structure for the binary search tree
###

class Node:

    #constructor
    def __init__(self, value = 0):
        
        #value of node, in this case an integer
        self.value = value

        #the right and left nodes pointing to
        #       root
        #     /      \
        #   left    right

        self.left:Node = None
        self.right:Node = None

    #getters and setters
    def getNode(self):
        return self
    
    def setNode(self, value = 0):
        self.value = value