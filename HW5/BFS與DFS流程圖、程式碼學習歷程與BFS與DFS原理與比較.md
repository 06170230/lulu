BFS與DFS流程圖、程式碼學習歷程與BFS與DFS原理與比較
===

BFS與DFS原理與比較
---

* BFS原理

    * 定義
    
        BFS (Breadth-First-Search) ——廣度優先搜尋,是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置，無論如何都要遍歷完畢整張地圖才終止。按照就         近原則進行，距離原點相同的節點的訪問順序是相近的。

        當在無權地圖中尋找最短的路徑的時候，不用出現大小比較

        因為尋找自起點開始，只要找到了某一個點，他一定是目前相同步數中距離起點最近的

        因為每一步都是從同一個節點開始 ，按照節點出現的順序（queue記錄）去尋找的，所以先出現的點，一定比後出現的點距離原點近。

        BFS使用　’queue‘　來進行儲存未被檢測的節點，利用佇列的先進先出的特點來按照寬度訪問查詢等待計算的節點。

        BFS　實現路徑記錄，可以每一次儲存遍歷節點的父節點，這樣的話，在輸出的時候就可以遍歷回溯到上一節點，從而實現路徑輸出。

* DFS原理

    * 定義
    
        DFS (Depth-First-Search)——深度優先搜尋，是從根節點開始，逐個訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個         回溯前驅節點。

        DFS 使用`stack`儲存未被檢測的節點，節點按照深度優先的次序被訪問並依次被壓入`stack`中，並以相反的次序出`stack`進行新的檢測。

        DFS使用 `stack `這一種資料結構來儲存未訪問的節點。



* BFS與DFS比較

dfs使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用dfs來實現相關問題。反之，在求最短路問題時，dfs需要反覆經過同樣的狀態，所以此時使用bfs為好。

bfs會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。反之，dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省記憶體。


[參考資料](https://www.itread01.com/content/1541297601.html)

[參考資料](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/#outline__1)

BFS
===

流程圖
---

<img src = "https://github.com/06170230/lulu/blob/master/image/.jpg" height =700 weight = 700>

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

[參考youtube影片](https://www.youtube.com/watch?v=QkEOGoUar3g)

DFS
===

流程圖
---

<img src = "https://github.com/06170230/lulu/blob/master/image/.jpg" height =700 weight = 700>

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

在寫完BFS後發現DFS也非常相似，就只是取的方法不同而已，所以覺得很簡單

首先先創造出兩個空的`array`，`visit_list`放走路路徑的點，`stack`放與點連接的其他點

依照BFS的拿法，我們會按照順序從`queue`最下面的數值開始拿，而DFS則是從`stack`最上面的數值開始拿

因此我這邊使用`stack.pop(-1)`，取最後一位

然後把我們pop出來的數加到`visit_list`中，紀錄我們已經走過這個點

接著搜尋`graph`中的其他連接點

如果已經有存在於`visit_list`或是`stack`之中，那我們就不用再加進來，因為我們已經走過這個點

使用迴圈重複上述的動作，直到graph中的數字都走過一次就完成啦！！

[參考youtube影片](https://www.youtube.com/watch?v=0Zsabo7ires&t=29s)
