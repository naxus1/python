import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data), end="")
        node = node.next
        if node:
            print(sep,end="")

#
# Complete the 'removeNodes' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST listHead
#  2. INTEGER x
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#


def removeNodes(listHead, x):
    # Write your code here
    headref = listHead
    nodeant = None
    while(headref):
        if headref.data > x:
            headref = headref.next
            #return listHead
        else:
            headref = headref.next
    return listHead

def delNodes(head,x): 
    current = head 
  
    # Initialize max 
    maxnode = head 
  
    while (current != None and 
           current.next != None) : 
  
        # If current is greater than max, 
        # then update max and move current 
        if (current.next.data >= maxnode.data) : 
            current = current.next
            maxnode = current 
          
        # If current is smaller than max,  
        # then delete current 
        else: 
            temp = current.next
            current.next = temp.next
         #free(temp)
    return head

def removeNodesNico(listHead, x):
    deln = listHead    
    if listHead is not None:
        if deln.data > x:
            listHead = listHead.next
            deln = None
    prev = listHead
    while prev is not None:
        deln = deln.next
        
        if deln.data >= x:
            prev.next = deln.next
            deln = None
        else:
            prev = deln

if __name__ == '__main__':
    listHead_count = int(input().strip())
    listHead = SinglyLinkedList()

    for _ in range(listHead_count):
        listHead_item = int(input().strip())
        listHead.insert_node(listHead_item)
    
    x = int(input().strip())
    result = removeNodesNico(listHead.head, x)
    print("///")
    print_singly_linked_list(result, '\n')
    print("")