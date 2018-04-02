# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:14:18 2018

@author: Meena
"""

strs = 'abcdefghijklmnopqrstuvwxyz'      #use a string like this, instead of ord() 
def shifttext():
    inp = input('Input string here: ')
    shift=int(input('input shift here: '))
    cstring = []
    for i in inp:                     #iterate over the text not some list
        if i in strs:                 # if the char is not a space ""  
            cstring.append(strs[(strs.index(i) + shift) % 26])    
        else:
            cstring.append(i)           #if space the simply append it to data
    output = ''.join(cstring)
    return output
shifttext()
