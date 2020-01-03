#!/usr/bin/env python
# coding: utf-8

# In[8]:


from collections import defaultdict
import sys 
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w]) 
        
    def minDistance(self, dist, sptSet): 
        min = sys.maxsize
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index 

    def Dijkstra(self, s): 
        dist = [sys.maxsize] * self.V 
        dist[s] = 0
        sptSet = [False] * self.V
        x={} 
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V):                 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    
        for node in range(self.V):
            x.update( {str(node) : dist[node]} )
        return x


    
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
        

    def Kruskal(self): 
        z = {}
        result =[] 
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parent = [] ; rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v)
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
        for u,v,weight in result: 
            u = str(u)
            v = str(v)
            z.update( {str(u+"-"+v):weight} )
        return z

