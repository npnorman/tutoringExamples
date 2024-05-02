####
# Author: Nicholas Norman (NPN)
# Date: May 2024
# Last Modified:
#   NPN May 2024
# 
# A basic binary search algorithm
###

from typing import List
import math

#binary search algorithm
def binarySearch(value:int, arr:List[int]):
    #goal: search for a certain value in a list
    #input: value to search for and array / subarray (sorted)
    #output: true or false (results)

    print("Checking:", arr)

    result = False

    #if array is length 0,1,2
    #base cases
    if (len(arr) == 0):
        #no more items
        result = False
    elif (len(arr) == 1):
        #base case
        if (arr[0] == value):
            result = True
        else:
            result = False
    elif (len(arr) == 2):
        #base case
        if (arr[0] == value or arr[1] == value):
            result = True
        else:
            result == False

    #keep searching
    else:

        #find median
        median = math.floor(len(arr)/2)

        #if value is median, base case
        if (value == arr[median]):
            result = True

        #if lower, search left half
        elif (value < arr[median]):
            result = binarySearch(value, arr[0:median])

        #if higher, search right half
        elif (value > arr[median]):
            result = binarySearch(value, arr[median + 1:len(arr)])
        
    return result

#this is the list to search
numbers = []

#lets add x numbers to it
x = 20 #numbers to add

for i in range(0, x+1):
    numbers.append(i)

#sort the list
numbers.sort()

#find the list
n = input("input a number to search for 0-20: ")
n = int(n)
res = binarySearch(n, numbers)
print(f"is {n} in the list?: {res}")
print(f"should be completed in O(log2({len(numbers)})) = {math.ceil(math.log2(len(numbers)))} steps")