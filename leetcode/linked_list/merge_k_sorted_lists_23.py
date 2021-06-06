#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:32:56 2021

@author: radhakrishna
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import log,floor
class Solution:
    def merge2Lists(self,lists: List[ListNode])->ListNode:
        c1=lists[0]
        c2=lists[1]
        
        l1=0
        l2=0
        d=None
        last_d=None
        while(c1 is not None or c2 is not None):
            if(c1 is None):
                if(l1==0 and l2==0):
                    d=c2
                else:
                    last_d.next=c2
                break
            elif(c2 is None):
                if(l1==0 and l2==0):
                    d=c1
                else:
                    last_d.next=c1
                break
            if(c1.val<c2.val):
                if(l1==0 and l2==0):
                    d=c1
                    last_d=d
                else:
                    last_d.next=c1
                    last_d=last_d.next
                l1=l1+1
                c1=c1.next
            else:
                if(l1==0 and l2==0):
                    d=c2
                    last_d=d
                else:
                    last_d.next=c2
                    last_d=last_d.next
                    
                c2=c2.next
                l2=l2+1
        return d
                
    def mergeKLists(self, d: List[ListNode]) -> ListNode:
        k=len(d)
        if(k==1):
            return d[0]
        elif(k==0):
            return None        
        steps=floor(log(k,2))
        for n in range(0,steps):
            temp=[]
            el=floor(k/(2**(n+1)))
            p=len(d)
            for j in range(0,el):
                if(p%2!=0 and j==el-1):
                    temp.append(self.merge2Lists([self.merge2Lists([d[2*j],d[2*j+1]]),d[2*(j+1)]]))
                else:
                    temp.append(self.merge2Lists([d[2*j],d[2*j+1]]))
                    

            d=temp
            
        return d[0]
        
                
                
            
            
            
        