# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:23:01 2019

@author: Lenovo
"""
import string

S = input("Enter statement to check: ")
ch = "".join(S.split()).lower()
srtd = "".join(sorted(ch))

loweraz = string.ascii_lowercase[:]
i=0

while(i<len(loweraz)-1):
    if loweraz[i] in srtd:
        i+=1
    else:
        break

if(i==25):
    print("YES")
else:
    print("NO")