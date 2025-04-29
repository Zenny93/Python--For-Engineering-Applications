#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:02:39 2022

@author: zanubhassan
"""

import random

heightsM =[]
#set length of list to 20
for i in range(0,20):
    #any random flost between 1.5 and 2.2
    x = round(random.uniform(1.5,2.2),2)
    heightsM.append(x)
print(heightsM)
    
#using list comprehension to convert vaues in meters to feet
ft = [(num/0.3048) for num in heightsM] 
print (ft)
#converting the ft to inches using list comprehension to loop through
#The % 1 is to get the decimalportion of the ft then we multiply that by 12 to convert to inches.
inches = [(num % 1  * 12) for num in ft]
print(inches)
#rounding the inches to 2 decimal places using list comprehension to loop through
resinches = [round(item,2) for item in inches]
print(resinches)
#converting the feet in floats to integers using list comprehension to loop through
ft_int = [int(item) for item in ft]
print(ft_int)
#converting the inches in floats to integers using list comprehension to loop through
inch_int = [int(item) for item in resinches]
print(inch_int)
#the zip function lets us loop through two different list
#Joining the heights in ft and inches together - this prints them in a new line
heightsFt = "\n".join("{}'{}".format(x,y) for x, y in zip(ft_int,inch_int))
print(heightsFt)
#converting the strings of heights in ft and inches to a list
newheightsFt = heightsFt.split()
print(newheightsFt)
#printing first and last elements of the heights in meter
print(heightsM.pop(0), heightsM.pop())
#printing the first and last elements of heightsFt
print(newheightsFt.pop(0),newheightsFt.pop())
