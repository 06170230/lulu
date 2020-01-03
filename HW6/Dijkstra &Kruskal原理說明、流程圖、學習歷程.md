Dijkstra &Kruskal原理說明、流程圖、學習歷程
===


Dijkstra &Kruskal原理說明
---


* Dijkstra原理

    最短路徑，尋找的答案是，給定一個基準點，要算出 "所有其他點" 到 "基準點" 的 "最短距離"

  * Dijkstra執行步驟
  
    1.從基準點開始，向外延伸一格能到達的所有vertex，並且從那些vertex當中，選一條路徑最短的

    2.再從剛剛選定的vertex向外延伸一格所有能到達的vertex，並且也是選一條路徑最短的

    3.重複2.這個步驟，直到每個vertex都被拜訪過，那麼最終的答案就出來了

    4.拜訪過的vertex就不會再重複拜訪了

    5.需要紀錄每個vertex的 "上一個節點" 或者是說parent，以便回頭尋找最短路徑所經過的點

    



* Kruskal原理

    最小生成樹，不需要給定基準點，而是會從權重(或是路徑)最小的path開始走訪，直到連成V-1條邊
   
  * Kruskal執行步驟
  
    1.先把所有path按照權重，從小到大排序

    2.需要一個表格來記錄每個edge所屬的 "subset" 或稱 "子集合" 至於子集合要用哪個edge當作代表 可以自行訂定一套規則

    3.每次都會從權重最小的path選一個，並且確認那兩個edge的subset不相同，才可以把這個path加入最小生成樹

    4.重複執行3.這個步驟，直到有V-1個path都被加入最小生成樹，那就可以停止了
    
 
 
 
 
 
 
 
 
 Dijkstra &Kruskal流程圖
 ---
 
 Dijkstra流程圖
 ---
 
 <img src = "https://github.com/06170230/lulu/blob/master/image/Dijkstra.jpg" height =700 weight = 700>
 
 Kruskal流程圖
 ---
 
 <img src = "https://github.com/06170230/lulu/blob/master/image/Kruskal1.jpg" height =800 weight = 800>
 
 <img src = "https://github.com/06170230/lulu/blob/master/image/Kruskal2.jpg" height =600 weight = 600>
 






Dijkstra &Kruskal學習歷程
---

* Dijkstra

```py
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
```

* Kruskal

```py
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
```

這次的作業我認為比之前困難許多，一開始雖然在上課就知道Dijkstra的運作模式

但是在真的寫程式的時候真的毫無頭緒，只能參考moodle裡老師給的資料，去理解Dijkstra的程式碼

光是理解Dijkstra就花了不少時間，再加上之後的Kruskal也很困難，所以也參考網路上的程式碼

不過我也有吸收下來，現在考完期末考了，我也有時間用自己的方法重新寫寫看！

Dijkstra參考資料 (https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

Kruskal參考資料 (https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
