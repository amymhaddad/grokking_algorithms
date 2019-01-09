#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

arr = [5, 3, 6, 2, 10]

def findSmallest(arr):
    """Find the index of the smallest element in a list"""

    #stores the VALUE at position 0 (when sorted, it'll be the smallest value). Right now arr[0] = 5
    smallest = arr[0]
    # #variable stores INDEX
    smallest_index = 0

    #cycle through each element in list, starting at 1
    for i in range(1, len(arr)):
        #arr[i] looks through each element in list in turn and compares it to "smallest"
        #ie: if 5 < 5 (which is arr[0])
        #ie: if 3 < 5...

        if arr[i] < smallest:
            #updating "smallest" variable. "smallest" now stores the VALUES that are less than arr[0] (ie, 5)
            #if 5 < 5 if 3 < 5 ... ---> cycle through entire list to compare arr[i] with "smallest"
            #smallest = 3 and 2
            smallest = arr[i]

            #update "smallest_index" variable to store the POSITION//INDEX of the smallest values
            #smallest_index = 1 and 3
            smallest_index = i

    return smallest_index

x = findSmallest(arr)

# print(x)

#sorting an array
def selectionSort(arr):
    newArr = []

    #get the index for each element
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(smallest)
        import pdb; pdb.set_trace()
    
    return newArr

x = selectionSort(arr)
print(x)
