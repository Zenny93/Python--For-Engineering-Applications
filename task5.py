    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 05:10:43 2022

@author: zanubhassan
"""

import re
import sys

# Our RE  line of code
pat = '\(?(\d{3})[-\)]?[-\s]?(\d{3})[-\s]?(\d{4})$'
# Compile the string into an RE command 
repat = re.compile(pat)
# Phone number to test on, provided as user input
mob_no = sys.argv[1]

# Search our input with RE module
search = repat.search(mob_no)

if search:
    # Print the three sets of numbers found
    print(f"""
    Area code: {search.groups()[0]}
    Exchange Code: {search.groups()[1]}
    Line extension: {search.groups()[2]}""")
else:
    # Print not found if the search failed
    print('Not Found')