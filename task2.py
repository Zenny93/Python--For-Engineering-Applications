#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:03:53 2022

@author: zanubhassan
"""

import pandas as pd
df2 =pd.read_pickle('IMDB-Movie-Data.pkl')
#print(df2)
#print number of empty rows in each column
print(df2.isnull().sum())

#since the count only shows that the numeric data were missing,
#will be replacing the missing numeric data with the avaerage of the entire column as asked
#in this assignment
#print(df2.fillna(df2.mean())) - could also be used but gives a warning about future type error
#so I chose this other method
#Finding the mean of the column having NaN

#for the revenue(millions column)
mean_value1=df2['Revenue (Millions)'].mean()
  
# Replace NaNs in column Revenue (Millions)with the
# mean of values in the same column
df2['Revenue (Millions)'].fillna(value=mean_value1, inplace=True)

#for metascore column
mean_value2=df2['Metascore'].mean()
  
# Replace NaNs in column metacsore with the
# mean of values in the same column
df2['Metascore'].fillna(value=mean_value2, inplace=True)
print(df2)

#finding the correlation between each of the quantitative columns
print(df2.corr(method = 'pearson'))

favDir = df2.loc[(df2['Director']== 'Denis Villeneuve')]
print(favDir)


#estimating the 25 % quantile of the revenue column
quantile_value =df2['Revenue (Millions)'].quantile(q=0.25)
print(quantile_value)

#Print the titles of all the movies of your favourite director that are above the 25% quantile
print (favDir['Title'][favDir['Revenue (Millions)'] > quantile_value])

#Print the mean rating of all the movies in the favDir dataframe
print(favDir['Rating'].mean())
