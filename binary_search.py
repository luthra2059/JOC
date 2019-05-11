# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:24:44 2019

@author: om8007
"""

#No of iterations = log2(no of elements in array)

def binary_search(a,x):
    first_pos = 0
    last_pos = len(a) - 1
    flag = 0
    count = 0
    while(first_pos <= last_pos and flag == 0):
        count+=1
        mid = (first_pos + last_pos)//2
        if(x==a[mid]):
            flag =1
            print("Element found at position:"+str(mid))
            print("No of iterations:"+str(count))
            return
        else:
            if(x<a[mid]):
                last_pos = mid-1
            else:
                first_pos = mid+1
    print("The number is not present")

a = []
for i in range(1,10001):
    a.append(i)
    
binary_search(a,8888)