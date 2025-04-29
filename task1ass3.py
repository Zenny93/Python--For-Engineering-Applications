# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
A = numpy.random.uniform(-1.0, 1.0, 1000000)
print(A)


#lIST B
B = [None]*500000
B = [num**2 for num in A[::-2]]
print(B)

  
#LISTC
C = []
for i in A[::-2]:
    
    # calculate square and add to the result list
    C.append(i * i)
print(C)

#LISTD
D = []
#starting at index 0
i = 0
#Just set A to look at other element first before doing my while loop

while i < len(A):
    if i % 2 !=0:
        D.append(A[i]**2)
        i = i + 1
    else:
        D.append(A[i])
        i = i + 1
print(D)
        
        
#time for B
import time
tic = time.process_time() #start watch
B = [None]*500000
B = [num**2 for num in A[::-2]]
toc = time.process_time() #stop watch
print(f"Elapsed time for B:{toc-tic:0.7f}s.")

#Print first and last elements of B
BLast=B.pop() # Removes last element
Bfirst =B.pop(0) #Removes first element
print(Bfirst, BLast)

#time for c
tic = time.process_time() #start watch
C = []
for i in A[::-2]:
    
    # calculate square and add to the result list
    C.append(i * i)
toc = time.process_time() #stop watch
print(f"Elapsed time for C:{toc-tic:0.7f}s.")

#Print first and last elements of C
CLast=C.pop() # Removes last element
Cfirst =C.pop(0) #Removes first element
print(Cfirst, CLast)


#time for D
tic = time.process_time() #start watch
D = []
#starting at index 0
i = 0
#Just set A to look at other element first before doing my while loop
while i < len(A):
    if i % 2 !=0:
        D.append(A[i]**2)
        i = i + 1
    else:
        D.append(A[i])
        i = i + 1
toc = time.process_time() #stop watch
print(f"Elapsed time for D:{toc-tic:0.7f}s.")

#Print first and last elements of D
DLast=D.pop() # Removes last element
Dfirst =D.pop(0) #Removes first element
print(Dfirst, DLast)

