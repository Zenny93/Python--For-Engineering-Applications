#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 04:18:41 2022

@author: zanubhassan
"""

import numpy
import time
#Create two lists A and B of 100,000 random floats between -10 and 10
A = numpy.random.uniform(-10.0, 10.0, 100000)
B = numpy.random.uniform(-10.0, 10.0, 100000)

#Do an element-wise sum to generate list C. In seperate lines, print the time taken for the
#sum, the first and last element of C

#Element wise addition of two lists
C = numpy.add(A,B).tolist()
#print(C)

#Print Time taken for the sum of C
tic = time.process_time() #start watch
C = numpy.add(A,B).tolist()
toc = time.process_time() #stop watch
print(f"Elapsed time for C:{toc-tic:0.7f}s.")

#Getting first and last element
CLast=C.pop() # Removes last element
Cfirst =C.pop(0) #Removes first element
print(Cfirst)
print(CLast)

#Now, convert the lists A and B into numpy arrays with the same name
A = numpy.array(A)


B= numpy.array(B)

#elementwise sumof the twonumpy arrays
C = A + B
#print(C)

#Print Time taken for the sum of C
tic = time.process_time() #start watch
C = A + B
toc = time.process_time() #stop watch
print(f"Elapsed time for C:{toc-tic:0.7f}s.")

#Getting first and last element
CLast=C[-1] # Removes last element
Cfirst =C[0] #Removes first element
print(Cfirst)
print(CLast)