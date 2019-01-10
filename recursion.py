#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""
 
i = 3
def countdown(i):
    print(i)
    #base case
    if i <= 0:
        return
    #recursive case    
    else:
        countdown(i-1)

x = countdown(i)

x = 3

def fact(x):
    #base case to stop the recursion
    if x == 1:
        return 1
    #recursive case: product * resutl of running same function on the number -1
    else: 
        return x * fact(x-1)

y = fact(x)
print(y)

