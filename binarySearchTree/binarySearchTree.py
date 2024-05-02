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
        self._root:Node = None

    #setters and getters
    def getRoot(self):
        return self._root
    
    def setRoot(self, root:Node):
        self._root = root

    #property to make .getRoot into .root
    root = property(getRoot, setRoot)

    #search
    def search(self, value, node:Node):
        #goal: search for given value in tree
        #input value and node
        #output: true or false value if found

        output = False #storing the results

        #if the root/node is null
        if (node == None):
            #return false nothing to find
            output = False
        
        #else if the value is the node
        elif (value == node.getValue()):
            #base case
            #return true
            output = True
        
        #else if the value is smaller
        elif (value < node.getValue()):
            #search left subtree
            output = self.search(value, node.left)

        #else if the value is bigger
        elif (value > node.getValue()):
            #search right subtree
            output = self.search(value, node.right)

        #catch
        else:
            print("not supposed to get here")
            output = False
        
        #return results
        return output


    #insert
    def insert(self, value:int, node:Node):
        #goal: insert this value into the tree
        #input: value and node
        #output: added to tree

        #search for the values position
        if (self._root == None):
            #no root yet, this is my root
            self._root = Node(value)
        
        #if the value is less than the nodes, move left
        elif (value < node.getValue()):
            
            #if left is null, base case, insert
            if (node.left == None):
                #base case
                node.left = Node(value)

            #else run this script again
            else:
                self.insert(value, node.left)

        #if the value is more than (or equal to) the nodes, move right
        elif (value >= node.getValue()):
            
            #if right is null, base case, insert
            if (node.right == None):
                #base case
                node.right = Node(value)

            #else run this script again
            else:
                self.insert(value, node.right)

    #delete
    def delete(self, value, node:Node):
        #goal: delete a value from the list
        #input: value and node
        #output: new root of tree/subtree

        output = None #stores new root of tree

        if (node == None):
            output = node

        #if the value is the node
        elif (node.getValue() == value):
            #base case
            #deleting here

            #case 1: deleting a leaf node
            if (node.left == None and node.right == None):
                #no children
                output = None
            
            #case 2: deleting a node with 1 child
            elif (node.left == None):
                #left is not there, set right to root
                output = node.right
            
            elif (node.right == None):
                #right is not there, set left to root
                output = node.left

            #case 3: deleteing a node with 2 children
            else:
                #right and left are there, 2 children
                #set the node to its successor (the node next in order), which is a leaf node

                #find successor
                successorParent = node #this makes it easier to delete
                successor = node.right
                current = node.right

                #while there is a smaller value
                while(current.left != None):
                    #make current the smaller value
                    successorParent = current
                    current = current.left

                    #make successor current
                    successor = current

                #make it the root
                node.setValue(successor.getValue()) #replace the value
                output = node

                #delete the successor
                if (successorParent.left == successor):
                    #move root up the chain
                    successorParent.left = successor.right

                elif (successorParent.right == successor):
                    #move root up the chain
                    successorParent.right = successor.right

        #if value is less
        elif (value < node.getValue()):
            #call function on subtree
            node.left = self.delete(value, node.left)
            output = node

        #if value is greater than
        elif (value > node.getValue()):
            #call value on subtree
            node.right = self.delete(value, node.right)
            output = node

        return output

    #basic printing algorithm for a tree
    def printTree(self, node:Node, level=0, prefix='Root: '):
        
        #prints tree
        if node is not None:
            print(' ' * (level * 4) + prefix + str(node.getValue()))
            if node.left is not None or node.right is not None:
                self.printTree(node.left, level + 1, 'L-- ')
                self.printTree(node.right, level + 1, 'R-- ')


if __name__ == "__main__":
    #test code

    #create a tree
    tree = BinarySearchTree()

    #insert some numbers
    tree.insert(10, tree.root)
    tree.insert(5, tree.root)
    tree.insert(15, tree.root)
    tree.insert(2, tree.root)
    tree.insert(7, tree.root)
    tree.insert(12, tree.root)
    tree.insert(11, tree.root)

    #print the tree to view
    tree.printTree(tree.root)

    #search for some numbers
    print("search for 10:", tree.search(10, tree.root))
    print("search for 3:", tree.search(3, tree.root))
    print("search for 12:", tree.search(12, tree.root))

    #delete some keys
    print("deleting node 5")
    tree.delete(5, tree.root) #root (2 children)
    #tree.delete(12, tree.root) #leaf node
    #tree.delete(15, tree.root) #1 child
    #tree.delete(1, tree.root) #None

    #print the tree to view
    tree.printTree(tree.root)