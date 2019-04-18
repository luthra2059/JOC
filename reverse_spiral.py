# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:20:26 2019

@author: om8007
"""

def reverse(m,n,arr):
    r = 0
    c = 0 
    
    while(r<m and c<n):
        for i in range(r,m):
            print(arr[i][c],end=" ")
            
        c+=1
        
        for i in range(c,n):
            print(arr[m-1][i],end=" ")
            
        m-=1
        
        if(c<n):
            for i in range(m-1,r-1,-1):
                print(arr[i][n-1],end=" ")
                
        n-=1
        
        if(r<m):
            for i in range(n-1,c-1,-1):
                print(arr[r][i],end=" ")
            
        r+=1
        
        
n = int(input("Enter value of n for nxn matrix:"))
arr=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    arr.append(l)
    
reverse(n,n,arr)
            
            