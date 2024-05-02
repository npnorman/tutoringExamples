####
# Author: Nicholas Norman (NPN)
# Date: May 2024
# Last Modified:
#   NPN May 2024
# 
# A basic binary search algorithm & binary search tree algorithm
###

import math

def guess():
    print("let me guess your number.")

    current = 50
    offset = 50

    keepGoing = True

    while(keepGoing):

        if (current > 100 or current < 0):
                keepGoing = False

        print(f"is it {current}?")

        user:str = input("(H)igher or (L)ower or (C)orrect: ")
        user = user.lower()

        offset = math.ceil(offset/2)

        if (user == "h"):
            #higher
            current += offset
        elif (user == "l"):
            #lower
            current -= offset
        elif (user == "c"):
            #correct
            keepGoing = False
        

guess()