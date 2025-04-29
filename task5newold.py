#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:37:37 2022

@author: zanubhassan
"""

import math
class Point:
    def __init__(self,x=0,y=0):
        #defining x and y variables
        self.X = x
        self.Y= y
        
    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)
    
    def getX(self):
        return self.X
    
        def getY(self):
            return self.Y
        
        def reflectX(self):
            x = self.X
            y = (-1) * self.Y
            return "Point(%s,%s)"%(x, y)
        
        def reflectY(self):
            x = (-1)*self.X
            y = self.Y
            return "Point(%s,%s)"%(x, y)
        
        def slope(self, other):
            dx = self.X - other.X
            dy = self.Y - other.Y
            return math.hypot(dx,dy)
        
        def getEq(self, point):
            y = self.Y
            dy = self.Y - point.Y
            x = self.X
            dx = self.X - point.X
            m = dy/dx
            c = y - (m*x)
            def g(x):
                ynew = (m*x) + c
                return ynew
            return g
        
            