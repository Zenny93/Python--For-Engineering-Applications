#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:03:51 2022

@author: zanubhassan
"""
#Write a function printSentences(sentenceNums), that takes as input a list of integers sentenceNums
#representing sentence numbers, and prints out the sentence corresponding 
#to the sentence number from The Time Machine by H.G.Wells(this is a txt file).
#Print each sentece on seperate lines
#
#line cache would read through entire memory
import linecache
def printSentences(sentenceNums):
 #we set lines = [] so that when we get the line we are looking for after 
 #looping through number given, we can put it in another list.
 #the append function adds something into another object
 lines =[]
 i = 0
 
 for i in sentenceNums:
    x = linecache.getline('time_machine_500.txt', i).strip()
  
    lines.append(x)
 print(*lines, sep = '\n') #This ensures the result of the list is printed in separate lines
 
 #zanub you tested this function by running printSentences([4,5]) in your console.
# could also be done in command line
    

