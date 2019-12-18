#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict

class Graph: 
    def __init__(self):  
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 
        visit_list = [] 
        queue = [s]
         
        while (len(queue) != 0):
            s = queue.pop(0)
            visit_list.append(s)
            for root in self.graph[s]:
                if root not in visit_list and root not in queue:
                    queue.append(root)    
        return visit_list
    
    def DFS(self, s):
        visit_list = []
        stack = [s]
        
        while (len(stack) != 0):
            s = stack.pop(-1)
            visit_list.append(s)
            for root in self.graph[s]:
                if root not in visit_list and root not in stack:
                    stack.append(root)   
        return visit_list

