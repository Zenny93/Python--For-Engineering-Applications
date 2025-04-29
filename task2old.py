#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 23:35:33 2022

@author: zanubhassan
"""
#Assume that: f is a continuous function; f(a) ·f(b) < 0 for some known values a and b; and
#a < b. Then, there exists some value c ∈(a, b) such that f(c) = 0. In other words, the function
#f has a root in the interval (a, b).
#f(a).f(b) < 0 means a and b have opposite times
#Thisfunction is the bisection/Intermediate value theorem method
def root(f, a, b, EPS):
    if f(a)*f(b) > 0:
        print('Root not found')
        c = (a+b)/2 #midpoint
        while c - a > EPS:
            if f(c) == 0:
                return c
            elif f(a)*f(c) > 0:
                a = c
            else:
                b = c
                c = (a+b)/2
            return c