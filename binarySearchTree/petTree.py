####
# Author: Nicholas Norman (NPN)
# Date: Apr 2024
# Last Modified:
#   NPN May 2024
# 
# A bst with Pet
###

from pet import *
from binarySearchTree import *

petTree = BinarySearchTree()

fido     = Pet(10, "fido")
tom      = Pet(5, "tom")
chippy   = Pet(15, "chippy")
poppy    = Pet(2, "poppy")
spots    = Pet(7, "spots")
red      = Pet(12, "red")
mrTurtle = Pet(11, "Mr. Turtle")
timmy = Pet(14, "Timmy") #not in list

pets = [fido, tom, chippy, poppy, spots, red, mrTurtle]

#insert these into the tree!
for pet in pets:
    petTree.insert(pet, petTree.root)

#view the tree
petTree.printTree(petTree.root)

#search for a pet
print("is spots in the tree?:", petTree.search(spots, petTree.root))
print("is timmy in the tree?:", petTree.search(timmy, petTree.root))