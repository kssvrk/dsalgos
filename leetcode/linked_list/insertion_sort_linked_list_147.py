#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:30:33 2021

@author: radhakrishna
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def adjust(self,head:ListNode)->ListNode:
        dh=ListNode()
        dh.next=head
        #insert in the starting so that it can be adjusted towards end.
        #left to right flow.
        #inserted value in starting. check if next node is smaller than this node etc.
        
        current=head
        prev=dh
        #print(dh)
        while(current and current.next):
            #print(dh)
            if(current.val>current.next.val):
                prev.next=current.next
                prev=current.next
                #print(prev.val)
                nex=current.next.next
                current.next.next=current
                current.next=nex
                
            else:
                break
        #print(dh.next)
        return dh.next
        
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        dh=ListNode(head.val)
        dh.next=None
        
        
        if(not head or not head.next):
            return head
        else:
            
            current=head.next
            
            c=0
            while(current):
                #print(current.val)
                #print(dh)
                d=current.next
                current.next=dh
                dh=self.adjust(current)
                current=d
            return dh
                
            