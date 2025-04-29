#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:35:25 2022

@author: zanubhassan
"""

import numpy
from numpy import linalg as LA

#Matrixof size 500 by 500 with random floats between -1.0 and 1.0
A =numpy.random.uniform(-1.0,1.0,size = (500,500))
print(A)
# setting axis = 0 signifies that we are summing the array over columns in a matrix
sumA = numpy.sum(A, axis=0)
print (sumA)

#multiplying A and A transpose
AAT = numpy.dot(A, A.T)
print(AAT)

#multiplyin A transpose by A
ATA = numpy.dot(A.T, A)
print(ATA)

#Getting the Frobenius norm of A
FrobA = LA.norm(A, 'fro')
print(FrobA)