#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:05:05 2022

@author: zanubhassan
"""
import pandas as pd
import matplotlib.pyplot as plt
#a scatter plotof rating vs revenue
df3 =pd.read_pickle('IMDB-Movie-Data.pkl')
plt.scatter(df3['Rating'],df3['Revenue (Millions)'])
plt.xlabel("Rating")
plt.ylabel("Revenue")
plt.title('Ratings vs Revenue(millions) plot')
plt.show()


#Plot the ratings vs revenue again but this time represent your favourite movie with a star
#and add the name of the movie in the legend
plt.scatter(df3['Rating'],df3['Revenue (Millions)'])
#defining theposition of Apocalypto
#from the csv file  the unamed column for Apocalypto is 232
variable = df3.iloc[232]
x = plt.scatter(variable['Rating'],variable['Revenue (Millions)'], marker = '*', label = 'Apocalypto')
plt.legend()
plt.xlabel("Rating")
plt.ylabel("Revenue")
plt.title('Ratings vs Revenue(millions) plot')
plt.show()
#plotting a histogram
#number of bins is 10 for a bin size of 1
plt.hist(df3['Rating'], density=True, bins=10)
plt.xlabel("Rating")
plt.ylabel("frequency")
plt.title('Ratings Histogram plot')
plt.show()