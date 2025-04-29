#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:15:59 2022

@author: zanubhassan
"""
import collections
from collections import Counter
#create an empty dictionary
d = dict()

#loop through each line of file
file = open("time_machine_500.txt", "r")
#loop through each lines in file
for line in file:
    
        #remove leading spaces and newline character
    line = line.strip()
 #convert characters in line to lowercase to avoid case mismatch
    line = line.lower()
 
 #remove punctuations
    line = line.replace('.','')
    line = line.replace(',','')
 #split the line into words
    words = line.split(" ")
 
 #remove punctuations
 
 
 
#f#or line in lines:
        #if line not in dict_count:
            #iterate over each word in line
    
    for word in words:
    
                #check if word is in the dictionary d
                if word in d:
        
                    #increment count of word by 1
                 d[word] = d[word] + 1
                else:
                    
            #add word to dictionary with a count of 1
                    d[word] = 1
                 
most_occur =  Counter.most_common(d,10)           
print(most_occur)

