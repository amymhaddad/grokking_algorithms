#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


def binary_search(list, item):
    """If item is in list, return position of item"""
    #Set parameters for search
    low = 0
    high = len(list) - 1

    #while low and high aren't the same...
    while low <= high:
        #find index for middle ele
        mid = (low + high) // 2
        #find value for middle ele
        guess = list[mid]

        #re-assign values for low and high below
        if guess == item:
            return mid
        if guess >= item:
            #change the high value, then start back at the top of the while loop
            high = mid - 1
        else:
            #change the low value, then start back at the top of the while loop
            low = mid + 1
    return None


x = binary_search(list, item)
print(x)
