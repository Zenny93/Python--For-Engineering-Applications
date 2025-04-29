#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:33:11 2022

@author: zanubhassan
"""
#a function that generates a file filled with random integers between range a and b and
#we have n random inetegers total
import random
def dataGen(n,a,b,fileName):
    for i in range(n):
       file = open(fileName + ".txt", "w")
       for i in range(n):
           values = random.randint(a, b)
           file.write(f"{i} {values}\n")
       file.close()

def dataRead(fileName):
    readFile = open(fileName + ".txt", 'r')
    values = []
    for line in readFile:
        values.append(line.split())
    return values
    readFile.close()
 
import itertools
def sumFile(fileName1,fileName2,k):
    lines = open(fileName1 + ".txt", 'r')
    words = open(fileName2 + ".txt", 'r')
    res = []
    for line, word in itertools.zip(lines, words):
        u = line.strip().split()
        v = word.strip().split()
        if u + v == k:
            res.append((u,v))
    return res
            
        
