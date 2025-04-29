#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:37:25 2022

@author: zanubhassan
"""
#Assignment 4 prob 1
import pandas as pd
import timeit
#reading the pickle file in a dataframe and printing it to make sure it works  
df = pd.read_pickle('IMDB-Movie-Data.pkl')
#print(df)

#estimating the time it takes to load the pickle file 1000 times
main_code_1 = """
import pandas as pd
df = pd.read_pickle('IMDB-Movie-Data.pkl')
"""

t1 = timeit.timeit(stmt = main_code_1,
                    number=1000)
print(f"Time to load the pickle file 1000 times is {t1}seconds")

#estimating the average time to load the pickle file once
print(f"Average time to load the pickle file once is {t1/1000}seconds")


#reading the pickle file in a dataframe and printing it to make sure it works  
df1 = pd.read_csv('IMDB-Movie-Data.csv')
#print(df1)
#estimating the time it takes to load the csv file 1000 times
main_code_2 = """
import pandas as pd
df1 = pd.read_csv('IMDB-Movie-Data.csv')
"""

t2 = timeit.timeit(stmt = main_code_2,
                     number=1000)
print(f"Time to load the csv file 1000 times is {t2}seconds")

 #estimating the average time to load the pickle file once
print(f"Average time to load the csv file once is {t2/1000}seconds")

main_code_3 = """
import pandas as pd
df = pd.read_pickle('IMDB-Movie-Data.pkl')
df.to_pickle("./IMDB-Movie-Data.pkl")
"""

t3 = timeit.timeit(stmt = main_code_3,
                     number=1000)

 #estimating the average time to write the pickle file once
 #you have to set index = False inthe to_csv function else your csv is overwritten with values.
print(f"Average time to write to the pkl file once is {t3/1000}seconds")

main_code_4 = """
import pandas as pd
df1 = pd.read_csv('IMDB-Movie-Data.csv')
df1.to_csv('IMDB-Movie-Data.csv', index = False)
"""

t4 = timeit.timeit(stmt = main_code_4,
                     number=1000)

 #estimating the average time to write the csv file once
print(f"Average time to write to the csv file once is {t4/1000}seconds")