#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:31:30 2021

@author: radhakrishna
"""

#19. Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        _=0
        if(n==0):
            return head
        
        c=head
        while(c):
            c=c.next
            _=_+1
        if(n==_):
            return head.next
        h=head
        c=0
        while(True):
            if(c+1==_-n):
                h.next=h.next.next
                break
            c=c+1
            if(h):
                h=h.next
        return head
#-------------- One pass solution------------------
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        k=0
        a=head
        if(not a):
            return None
        while(k<n-1):
            a=a.next
            k=k+1
        #----------a stopped at n-1 index , nth element
        b=head
        dh=ListNode()
        dh.next=b
        prev=dh
        #b and a advancing 1 each time till a ends and b should be deleted
        
        while(a.next):
            a=a.next
            prev=b
            b=b.next
        prev.next=b.next
        return dh.next