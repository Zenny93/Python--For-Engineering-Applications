#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
ch = sys.argv[1]
n = int(sys.argv[2])
if ord(ch)<97 or ord(ch)>122:
    print('Input Value Not Suppported. Program Exiting...')
    sys.exit()
def char_position(ch):
    return ord(ch) - 97

strt = char_position(ch)



def pos_to_char(n, strt):
    n = n%26
    result = n+97+strt
    if n+97+strt > 122:
        result = n+97+strt-26
        
    elif n+97+strt < 97:
        result = n+97+strt+26
            
    return chr(result)
pos_end = pos_to_char(n,strt)

print(pos_end)
