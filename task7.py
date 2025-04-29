#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:02:12 2022

@author: zanubhassan
"""

import time
def approach1():
 tic = time.process_time() #start watch
 for i in range(5000):
  x = (i**2)/21.3
 toc = time.process_time() #stop watch
 print(f"Elapsed time:{toc-tic:0.7f}s.")
 tic1 = time.process_time() #start watch
 for i in range(5000):
  y = (i**2)/32
 toc1 = time.process_time() #stop watch
 print(f"Elapsed time:{toc1-tic1:0.7f}s.")

def approach2():
 tic = time.perf_counter() #start watch
 for i in range(5000):
  x = (i**2)/21.3
 toc = time.perf_counter() #stop watch
 print(f"Elapsed time: {toc - tic:0.7f} s with perf_counter.")
 tic1 = time.perf_counter() #start watch
 for i in range(5000):
  y = (i**2)/32
 toc1 = time.perf_counter() #stop watch
 print(f"Elapsed time: {toc1 - tic1:0.7f} s with perf_counter.")
  
import timeit

def approach3():
#setup_code_1
 #impMath = "import math"

 main_code_1 = """
def compute(x):
 for i in range(5000):
   x =(i**2)/21.3
 return x
"""

 t1 = timeit.timeit(stmt = main_code_1,
                    number=1000)

#setup_code_2
#impMath1 = "import math"

 main_code_2 ="""
def compute(y):
 for i in range(0,5000):
   y=(i**2)/32
 return y
"""

 t2 = timeit.timeit(stmt=main_code_2,
                    number=1000)

 print(f"1000 runs of For Loop1 is {t1}seconds")


 print(f"1000 runs of For Loop2 is {t2}seconds")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--choice', type=int, required=True, \
        help='Select 1 or 2 to experiment two different types of timing')
    args = parser.parse_args()
    if args.choice == 1:
        approach1()
    elif args.choice == 2:
        approach2()
    elif args.choice == 3:
        approach3()
    else:
        print("argument list no ok.")
