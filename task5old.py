#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:42:53 2022

@author: zanubhassan
"""
#Write a function middle(a) that takes a list a and returns a new list that contains all but the
#first and last elements

#The list pop inbuilt function in python removes item from a specified index of a list
#it only takes in the index as a parameter
#When no index is specified,it removes last element of the list
def middle(a):
  a.pop() # Removes last element
  a.pop(0) # Removes first element
  return a


#How I tested my code.
#a = [1,2,3,4,5,6]

#print(middle(a)) # [2, 3, 4, 5]