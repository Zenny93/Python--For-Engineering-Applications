#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:01:45 2022

@author: zanubhassan
"""

annualsalary = float(input('Input annual salary:​ ')) #salary for the whole year
savingrate = float(input('Input saving rate, as a decimal: ​')) #the percentage of what you hope to save monthly
carprice = float(input('Input the cost of the car: ​'))    #total cost of the car

#Variables. All amounts in (#)
currentsavings = 0  #the amount saved so far,starting from 0
down_payment = 0.40 * carprice
r = 0.06 #annual rate
annual_return = (currentsavings * r) / 12
monthlysalary = annualsalary / 12
savingrate  = savingrate  * monthlysalary 
time = 0

#Iterations and Output
while (currentsavings<= down_payment):
    time += 1
    currentsavings+= (currentsavings * r / 12) + savingrate    
print('Number of months: %d'%time)