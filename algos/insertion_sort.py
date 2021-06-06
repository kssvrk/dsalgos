#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:50:33 2021

@author: radhakrishna
"""


def insertion_sort(num):
    
    if(len(num)==0):
        return num
    sorted_list=[num.pop(0)]
    if(len(num)==0):
        return sorted_list
    
    for k in range(0,len(num)):
        
        sorted_list.append(num[k])
        x=len(sorted_list)-1
        while(x>=1):
            
            if(sorted_list[x]<sorted_list[x-1]):
                sorted_list[x-1],sorted_list[x]=sorted_list[x],sorted_list[x-1]
            
            x=x-1
    print(sorted_list)
    
if(__name__=='__main__'):
    num=[8,9,10,2,3,4,12]
    num=[0,0,0,0,0,0,0,0]
    
    insertion_sort(num)