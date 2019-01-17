#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


list = [1, 3, 5, 7, 9]
item = -1

def binary_search(list, item):
    """If item is in the list, return the position of the item"""

    #set parameters of what I'm searching
    low = 0
    high = len(list)-1

    #while I haven't narrowed down the value to one element...
    while low <= high:
        #mid = find the index (position) of the middle element
        #guess = the value of the middle element. Using guess to compare with "item" that I'm passing in
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid + 1
        else:
            low = mid -1
    return None

x = binary_search(list, item)
print(x)
            
