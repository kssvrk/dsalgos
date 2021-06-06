#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:31:30 2021

@author: radhakrishna
"""

#19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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