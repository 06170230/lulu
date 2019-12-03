#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = h.hexdigest()
        key = int(h.hexdigest(),16)        
        index = key % self.capacity #看餘數
        node = self.data[index]
        
        if node is None:
            self.data[index] = ListNode(key)
            return        
        else:
            new_node = ListNode(key)
            while node.next != None:
                node.next = node.next.next
            node.next = new_node

        
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = h.hexdigest()
        key = int(h.hexdigest(),16)
        index = key % self.capacity
        node = self.data[index]
        
       
        if node!= None and node.val == key:
            self.data[index] = node.next
            return
        pre_node = None     
        while node.next:
            if node.next == key:
                pre_node.next = node.next
                return
            pre_node = node
            node.next = node.next.next
            return
                   
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = h.hexdigest()
        key = int(h.hexdigest(),16)
        index = key % self.capacity
        node = self.data[index]
        
        if node is None:
            return False
        else:
            if node.val == key :
                return True
            else:
                while node.next:
                    if node.next == key:
                        return True
                    node.next = node.next.next
                return False

