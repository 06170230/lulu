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
 
