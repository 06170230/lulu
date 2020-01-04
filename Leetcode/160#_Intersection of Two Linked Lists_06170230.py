#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        A_pointer = headA
        B_pointer = headB

        while A_pointer != B_pointer:
            A_pointer = headB if A_pointer == None else A_pointer.next
            B_pointer = headA if B_pointer == None else B_pointer.next

        return A_pointer

