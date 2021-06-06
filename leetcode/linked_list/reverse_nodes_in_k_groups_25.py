#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:32:33 2021

@author: radhakrishna
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil,floor,log
class Solution:

    def reverse(self,h:ListNode,size:int):
        #revrse the links of each node.
        current=h
        previous=None
        nex=current.next
        k=0
        while(k!=size):
            k=k+1
            current.next=previous
            previous=current
            
            current=nex
            if(nex is not None):
                nex=nex.next
            
        return previous
    
#brilliant me knows only merge sort so every where merge sort strategy
#         d=self.explode(h,size)
#         l=len(d)
#         for j in range(0,floor(log(l,2))):
#             el=floor(l/2**(j+1))
#             k=[]
#             for n in range(0,el):
#                 print(el,j,n)
#                 if(len(d)%2!=0 and n == el-1):
#                     #print(d[2*n],d[2*n+1])
#                     print('wow')
#                     self.merge_2reversed([d[2*n],d[2*n+1]])
#                     k.append(self.merge_2reversed([d[2*n+1],d[2*n+2]]))
#                 else:
#                     k.append(self.merge_2reversed([d[2*n],d[2*n+1]]))
#             d=k
#             print(d)
            
#         return d
                    
            
    def merge_2reversed(self,lists:List[ListNode]): #size of each list being sent
        l1=lists[0]
        l2=lists[1]
        current=l2
        k=0
        while(current.next is not None):
            current=current.next
        current.next=l1
        return l2        
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        current=head
        if(k<=1):
            return current
        leave_last=None
        #store each k hedas in array takes O(n)
        g=[]
        e=[]
        b=0
        while(b!=1):
        
            
            for ll in range(0,k):
                if(ll==0):
                    g.append(current)
                if(ll==k-1):
                    e.append(current)
                if(current.next is None):
                    if(ll!=k-1):
                        leave_last=g.pop()
                    b=1
                    break
                
                
                current=current.next
                
        l=len(g)
        #print(g)
        h=None
        #print("L"+str(l))
        for x in range(0,l):
            d=g[x]
            y=self.reverse(d,k)
            #print(y)
            if(x<l-1):
                g[x].next=e[x+1]
            else:
                g[x].next=leave_last
        #print(leave_last)
        return(e[0])
        
    
                
                
            
            
                