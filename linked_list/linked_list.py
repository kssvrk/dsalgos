#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:58:37 2021

@author: radhakrishna
"""

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next_node=None
    def __repr__(self):
        return f"Node : data {self.data}"

class LinkedList:
    
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head==None
    def size(self):
        """
        Counts the number of nodes in linked list by 
        sequential traversal.
        
        Time : O(n)

        """
        count=0
        current=self.head
        while current:
            count=count+1
            current=current.next_node
        return count
    def add(self,data,position):
        
        count=0
        updated=None
        if(position==0):
            d=self.head 
            self.head=Node(data)
            self.head.next_node=d
            updated=1
            #print(f" Added {self.head} at position {position}")
        else:
            current=self.head    
            while current:
                count=count+1
                if(position==count):
                    d=current.next_node
                    current.next_node=Node(data)
                    current.next_node.next_node=d
                    updated=1
                    #print(f" Added {current.next_node} at position {position}")
                    break
                current=current.next_node
        
        if(updated is None):
            raise IndexError(" Given position is out of range")
    def traverse(self,position):
        current=self.head 
        count=0
        while current:
            if(count==position):
                return current
            current=current.next_node
            count=count+1
        raise IndexError(" Given position is out of range")
    def __repr__(self):
        nodes=[]
        current=self.head 
        count=0
        while current:
            if(count==0):
                nodes.append(f"Head : {current.data} ")
            elif(current.next_node==None):
                nodes.append(f"Tail : {current.data} ")
            else:
                nodes.append(f"Node :{current.data} ")
            current=current.next_node
            count=count+1
        return '=> '.join(nodes)
    def search(self,data):
        current=self.head
        count=0
        while current:
            
            if(current.data==data):
                return count
            current=current.next_node
            count=count+1
        raise Exception(" Given data not available in the linked list")
    def delete(self,position):
        
        updated=None
        if(position==0):
            if(self.is_empty()):
                raise IndexError(" Given position is out of range")
            print(f" removing {self.head} at position {position}")
            d=self.head 
            self.head= d.next_node 
            updated=1
            
        else:
            current=self.head
            count=1
            while current:
                if(count==position and (current.next_node is not None)):
                    print(f" removing {current.next_node} at position {position}")
                    current.next_node=current.next_node.next_node
                    updated=1
                    
                    break
                count=count+1
                current=current.next_node
                
        if(updated is None):
            raise IndexError(" Given position is out of range")
    def has_cycle(self):
        slow=self.head
        fast=self.head 
        c=0
        while (slow.next_node is not None and fast.next_node is not None and fast.next_node.next_node is not None):
            slow=slow.next_node
            fast=fast.next_node.next_node 
            if(slow==fast):
                print(slow.next_node.data)
                c=1
                print('HAS CYCLE')
                break
        if(c!=1):
            print('LL HAS NO CYCLES')
    def reverse(self):
        #revrse the links of each node.
        current=self.head 
        previous=None
        nex=current.next_node 
        
        while(current is not None):
            current.next_node=previous
            previous=current
            
            current=nex
            if(nex is not None):
                nex=nex.next_node
            
        self.head=previous
if(__name__=='__main__'):
    ll=LinkedList()
    ll.add(0,0)
    ll.add(2,1)
    ll.add(4,2)
    ll.add(8,3)
    ll.add(16,4)
    ll.add(32,5)
    ll.add(64,6)          