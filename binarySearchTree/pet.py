####
# Author: Nicholas Norman (NPN)
# Date: Apr 2024
# Last Modified:
#   NPN May 2024
# 
# A custom data type to sort in my binary search tree, overloading
###

class Pet:
    #constr
    def __init__(self, age = 0, name = "Fido"):
        self.age = age
        self.name = name

    def __repr__(self):
        #representation as a string
        return f"name: {self.name}, age: {self.age}"

    #I want to compare these pets based on their age
    #I can overload the < > <= >= == operators to be able to sort them!
    # https://docs.python.org/3/reference/datamodel.html

    # x > y
    def __lt__(self, other):
        output = self.age < other.age
        return output
    
    # x >= y
    def __le__(self, other):
        output = self.age <= other.age
        return output
    
    # x < y
    def __gt__(self, other):
        output = self.age > other.age
        return output
    
    # x <= y
    def __ge__(self, other):
        output = self.age >= other.age
        return output
    
    # x == y
    def __eq__(self, other):
        output = self.age == other.age
        return output
    
    # x != y
    def __ne__(self, other):
        output = self.age != other.age
        return output
    


if __name__ == "__main__":
    #test code    
    fido = Pet(5, "Fido")
    chippy = Pet(5, "Chippy")
    tom = Pet(7, "Thomas")
    spots = Pet(1, "Spots")
    
    print(f"({fido})  > ({tom}) :",fido  >  tom) #false
    print(f"({spots}) > ({tom}) :",spots >= tom) #false
    print(f"({spots}) > ({fido})   :",spots <  fido) #true
    print(f"({fido})  > ({chippy}) :",fido  <= chippy) #true 
    print(f"({fido})  > ({chippy}) :",fido  == chippy) #true
    print(f"({fido})  > ({tom}) :",fido  !=  tom) #true