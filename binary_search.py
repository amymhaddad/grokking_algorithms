#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


numbers = [1, 3, 5, 7, 9]
item = 9

#function takes a sorted list and an item. If the item is in the list, then the function returns its position.

def binary_search(list, item):
    """If item is in list, return the position of the item"""

    #low and high below set the parameters of the list 
    #the index of the lowest position of a sorted list = 0
    low = 0
    #the index of the highest position of a sorted list
    high = len(list)-1


    while low < high:
        #find the INDEX of the middle position. ex: [1, 3, 5, 7, 9] ---> mid = 2
        mid = (low + high) // 2
        #guess finds the VALUE of the middle position ex: [1, 3, 5, 7, 9] ---> guess = 5
        guess = list[mid]

        #if guess (the value of the middle position) equals the item (the number you're passing in)
        if guess == item:
            #returning "mid" b/c they're equal and we're trying to find the position
            return mid

        #if guess (the value of the middle position) is greater than the item (the number you're passing in), then guess is too high
        #ie: [1, 3, 5, 7, 9] so guess = 5 and item = 1
        if guess > item:
            #guess is too high, so cut off the top 1/2 of the list and will only look at the bottom 1/2
            #so now the list looks like this: [1, 3, 5]. ie, move the starting search value to the left.
            high = mid - 1
        else:
            #If guess is too low, the bottom 1/2 of list is cut off and only looks at top 1/2. ie, move the starting search value to the right.
            low = mid + 1
    
    #item isn't in list
    return None
            
x = binary_search(numbers, item)

print(x)

