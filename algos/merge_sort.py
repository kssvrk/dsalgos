#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:04:59 2021

@author: radhakrishna
"""
from math import log,floor,ceil

#implement linked list merge sort
#implement recursive solution

def merge(sl1,sl2):
    d=[]
    c1=0
    c2=0
    l1=len(sl1)
    l2=len(sl2)
    while (c1<l1 or c2<l2):
        if(c1==l1):
            d.extend(sl2[c2:])
            c2=l2
        elif(c2==l2):
            d.extend(sl1[c1:])
            c1=l1
        elif(sl1[c1]<sl2[c2]):
            d.append(sl1[c1])
            c1=c1+1
        else:
            d.append(sl2[c2])
            c2=c2+1
    return d

def sort(num):
    #bottom to top approach for iterative
    l=len(num)
    d=[]
    for n in range(0,l):
        d.append([num[n]])
    for j in range(1,ceil(log(l,2))):
        step=2**j
        k=[]
        elements=floor(l/(step))
        #ep=l%%
        for n in range(0,elements):
            #print(n,step,elements,d)
            
            # for handling odd number of elements in d
            if(len(d)%2!=0 and n==elements-1):
                t=merge(d[2*n],d[2*n+1])
                k.append(merge(t,d[2*n+2]))
            else:
                k.append(merge(d[2*n],d[2*n+1]))
            print(n,step,k)
        d=k
    return d
                
    
            
        
if(__name__=='__main__'):
    numbers=[5,6,7,8,9,1,2,3,4,10,1,2,5.5,22,33,5,7,0.2,-9,231231]
   
    l1=[12,14,18,22]
    l2=[13,15,56,98,109,789,10003]

    #d=merge(l1,l2)
    #print(d)
    
    d=sort(numbers)
    
        
        