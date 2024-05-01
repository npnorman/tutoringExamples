####
# Author: Nicholas Norman (NPN)
# Date: Apr 2024
# Last Modified:
#   NPN May 2024
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
    
    def getValue(self):
        return self.value
    
    def setValue(self, value = 0):
        self.value = value

    def setLeft(self, left):
        #passing in a Node
        self.left = left

    def getLeft(self):
        return self.left
    
    def setRight(self, right):
        #passing in a Node
        self.right = right

    def getRight(self):
        return self.right
    
if __name__ == "__main__":
    #test code
    node = Node()

    #set its value
    node.setValue(5)

    #check it
    print("node value: ",node.getValue())

    #add a left and right
    leftNode = Node(17)
    rightNode = Node(2004)

    node.setLeft(leftNode)
    node.setRight(rightNode)

    #check all values
    print(f"root = {node.getValue()}\n--- L = {node.getLeft().getValue()}\n--- R = {node.getRight().getValue()}")