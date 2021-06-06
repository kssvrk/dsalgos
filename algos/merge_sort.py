#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:04:59 2021

@author: radhakrishna
"""
from math import log,floor,ceil
from linked_list.linked_list import LinkedList,Node

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
             
def llmerge(ll1,ll2):
    l1=ll1.size()
    l2=ll2.size()
    c1=0
    c2=0
    ll=LinkedList()
    count=0
    while(c1<l1 or c2<l2):
        #print(count,c1,c2,l1,l2)
        if(c1<l1 and c2<l2):
            d1=ll1.traverse(c1).data
            d2=ll2.traverse(c2).data
        if(c1==l1):
           ll.traverse(count-1).next_node=ll2.traverse(c2)
           c2=l2
        elif(c2==l2):
            ll.traverse(count-1).next_node=ll1.traverse(c1)
            c1=l1
            
        elif(d1<d2):
            ll.add(d1,count)
            c1=c1+1
        else:
            ll.add(d2,count)
            c2=c2+1
        
        count=count+1
    return ll
        
def llsort(ll):
    
    d=[]
    current=ll.head
    size=0
    while current:
        size=size+1
        ll=LinkedList()
        ll.add(current.data,0)
        d.append(ll)
        current=current.next_node
    #print(d)
    for j in range(1,ceil(log(size,2))):
        k=[]
        elements=floor(size/2**j)
        for n in range(0,elements):
            #print(n,j,size,d)
            if(len(d)%2!=0 and n==elements-1):
                t=llmerge(d[2*n],d[2*n+1])
                k.append(llmerge(t,d[2*n+2]))
            else:
                k.append(llmerge(d[2*n],d[2*n+1]))
        d=k
    return d

def recursive_mergesort(num):
    print(num)
    l=len(num)
    if(l<=1):
        return num
    left=num[:floor(l/2)]
    right=num[floor(l/2):]
    
    return merge(recursive_sort(left),recursive_sort(right))
    
        
if(__name__=='__main__'):
    
    #----- Numbers --------------------
    #numbers=[5,6,7,8,9,1,2,3,4,10,1,2,5.5,22,33,5,7,0.2,-9,231231]
    #l1=[12,14,18,22]
    #l2=[13,15,56,98,109,789,10003]
    #d=merge(l1,l2)
    #print(d)
    #d=sort(numbers)
    #-----------------------------------
    
    #------- LINKED LIST-----------
    # ll1=LinkedList()
    # ll1.add(50,0)
    # ll1.add(51,1)
    # ll1.add(80,2)
    # ll1.add(100,3)
    # ll1.add(190,4)
    
    # ll2=LinkedList()
    # ll2.add(100000,0)
    # ll2.add(21000,1)
    # ll2.add(1050,2)
    # ll2.add(2220,3)
    # ll2.add(3090,4)
    # ll2.add(-3090,5)
    # ll2.add(390,6)
    # ll2.add(30.90,7)
    # ll2.add(309**0,8)
    # ll2.add(3,9)
    # ll2.add(1,10)
    
    # #d=llmerge(ll1,ll2)
    # print('---------------------------')
    # e=llsort(ll2)
    #------------------------
    
    #---------------- recsort--------------
    numbers=[5,6,17,8,9,1]
    d=recursive_mergesort(numbers)
    
    #--------------------------------
        
        