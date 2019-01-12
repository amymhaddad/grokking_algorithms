#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

arr = [5, 3, 6, 2, 10]

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# x = findSmallest(arr)

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        #from the unsorted list, pop off the smallest element in the list
        #popped off and added to the sorted list
        #It knows to put it in order b/c the number with the smallest index is popped off first...
        #Append always puts it on the end, so always left to right
        newArr.append(arr.pop(smallest_index))
    return newArr
x = selectionSort(arr)
print(x)
