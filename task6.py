#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 06:58:36 2022

@author: zanubhassan
"""

#built in class method/attribute examples
class Animals:
    'This is a sample class for animals'
    def __init__(self):
        print("Hello from __init__ method.")
# class built-in attribute
print(Animals.__name__)
print(Animals.__module__)
