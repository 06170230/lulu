BFS與DFS流程圖、程式碼學習歷程與BFS與DFS原理與比較
===

BFS與DFS原理與比較
---

BFS
===

流程圖
---

<img src = "https://github.com/06170230/lulu/blob/master/image/BFS.jpg" height =700 weight = 700>

程式碼
---

```py
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
```

學習歷程
---

首先我先創造出兩個空的`array`，`visit_list`放走路路徑的點，`queue`放與點連接的其他點

依照BFS的拿法，我們會按照順序從`queue`最下面的數值開始拿，因此我這邊使用`queue.pop(0)`

然後把我們pop出來的數加到`visit_list`中，紀錄我們已經走過這個點

接著搜尋`graph`中的其他連接點

如果已經有存在於`visit_list`或是`queue`之中，那我們就不用再加進來，因為我們已經走過這個點

使用迴圈重複上述的動作，直到graph中的數字都走過一次

* 一開始錯誤的地方

<img src = "https://github.com/06170230/lulu/blob/master/image/bfswrong.jpg" height =500 weight = 500>

這是我一開始寫完後跑測值的結果，[2,2,0,3,1,3]

但正解其實是[2,0,3,1]

發現多一個2的問題是出在一開始`visit_list.append(s)`已經加過一次，後面又加了一次

最後面的3則是因為我pop掉3以後沒有馬上append進visit_list中，

所以在跑for迴圈的時候queue和visit_list中都沒有3，才會跑了兩次

經過修改以後就正確啦！！

DFS
===

流程圖
---

<img src = "https://github.com/06170230/lulu/blob/master/image/DFS.jpg" height =700 weight = 700>

程式碼
---

```py
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
```

學習歷程
---




