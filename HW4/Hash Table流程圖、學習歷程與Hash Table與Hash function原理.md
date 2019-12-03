Hash Table流程圖、學習歷程與Hash Table與Hash function原理
===

Hash Table原理
---

Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」

資料存放的方式是，資料經過md5處理後會轉成一串數值，這串數值除以table的長度，除出來的餘數對應我們要放置在Table (index)的何處

也因為這個方式所以  【很可能發生Collision】 

Collision就是兩筆資料存進同一個Table之slot的情形，這將會使得查詢資料失敗(例如：使用item1的Key，卻回傳item2的資料)。

為了解決這個問題，我們必須把該位置的資料作串聯，才能讓同個Table中的資料都能被保存

[Hash Table原理參考資料](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#ht)

[Collision參考資料](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#collision)

Hash function原理
---

優秀的Hash Function(h())應具備以下特徵：

* 定義h()的定義域(domain)為整個Key的宇集合U，值域(range)應小於Table的大小m：

* 盡可能讓Key在經過Hash Function後，在值域(也就是Table的index)能夠平均分佈(uniform distributed)，如此才不會有「兩筆資料存進同一個Table空格(稱為slot)」的情況。

若把Table想像成「書桌」，slot想像成書桌的「抽屜」

那麼為了要能更快速找到物品，當然是希望「每一個抽屜只放一個物品」

如此一來，只要拿著Key，透過Hash Function找到對應的抽屜(Hash Function的功能是指出「第幾個」抽屜，也就是抽屜的index)

就能保證是該Key所要找的物品

反之，如果同一個抽屜裡有兩個以上的物品時，便有可能找錯物品

* Division Method做法 :

要把大範圍的|U|對應到較小範圍的{0,1,...,m−1}，最直覺的做法就是利用%取餘數。

假設Table大小為m，定義Hash Function為：

h(Key)=Key%m

例如，選定Table大小為m=8，那麼以下的Key與Table之index將有對應關係如下：

* h(14)=14%8=6
    * 代表「編號14」的物品要放進「第6格」抽屜。
* h(23)=23%8=7
    * 代表「編號23」的物品要放進「第7格」抽屜。
* h(46)=46%8=6
    * 代表「編號46」的物品要放進「第6格」抽屜。
* h(50)=50%8=2
    * 代表「編號50」的物品要放進「第2格」抽屜。

[Hash function原理參考資料](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#hf)

[Division Method參考資料](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#dm)

Hash Table 流程圖、學習歷程
---

我覺得這次`Hash Table`對我來說比之前的作業容易，因為會運用以前的`Binary search tree`節點連接的觀念

差異就在`Binary search tree`有分成left跟right，而`Hash Table`是一條線連接下去



add
---

首先我們要考慮的是，當我們把key值對應到index時，可能會出現同個index有一個以上的key值情況發生

這時如果我們不做處理，那麼key值就會一個一個互相取代掉彼此

因此我們要把所有對應到同個index的key值都保存下來

我直接把他當成是`Binary search tree`的insert來做

該index如果頭的node是空值，那我們就能直接把key加在頭node

如果頭node不是空值，那我們就寫一個while迴圈

直到找到下面連接的node是空值的時候，就可以加進去

```py
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
```

* 錯誤情形

    * 如果同個index中有多於一個以上的key值而不做處理會發生這個情況

<img src = "https://github.com/06170230/lulu/blob/master/image/hashtable_add.jpg" height =750 weight = 750>

* 正確情形

    * 把同個index中的所有key值做串聯，讓他們一個都不會少

<img src = "https://github.com/06170230/lulu/blob/master/image/hashtable_add2.jpg" height =750 weight = 750>

[參考資料](https://www.youtube.com/watch?v=zHi5v78W1f0&t=3s)

[參考資料](https://www.youtube.com/watch?v=vBxmYemGUWk&t=561s)

參考資料 : 老師上課教的內容

remove
---

一開始在寫remove的時候也還算順利，不過寫完以後發現有錯誤但一直找不到問題

重新多看好幾次後發現如果我再刪除某個key值時，就只是單純把他刪除

但如果index中還有其他node也被串聯在被刪除的key值後面，那麼整個連接就會斷掉

因為index中可能有大於一個以上的node，我們做刪除後，必須把後方串聯好的node遞補上來

因此先寫一個刪除node後，後方的node遞補上去的程式

```py
        if node!= None and node.val == key:
            self.data[index] = node.next
            return
```

代表node.next遞補成第一個node了

接著寫while迴圈

一層一層往下看直到我們找出要刪除的key值

直到整串index中的node都被走訪過一次

如果找不到要刪除的key值就直接回傳


```py
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
```

* 錯誤情形 
    * 當我們沒有寫遞補程式時

<img src = "https://github.com/06170230/lulu/blob/master/image/hashtable_remove.jpg" height =700 weight = 700>

* 正確情形
    * 經過遞補後的
    
<img src = "https://github.com/06170230/lulu/blob/master/image/hashtable_remove2.jpg" height =700 weight = 700>

[參考資料](https://www.youtube.com/watch?v=O4dGJZ4J0Bk)

參考資料 : 老師上課教的內容


contains
---

contains 我也是把他當成 `binary search tree` 中的search來看

從node的頭開始找如果node是None就直接回傳False

如果node的值剛好等於key值就回傳True

或是繼續往下找一層一層找，使用while迴圈

走過每個下面的node直到走完，如果有找到則回傳True

如果沒有找到就回傳False


```py
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
```

<img src = "https://github.com/06170230/lulu/blob/master/image/hashtable_contains.jpg" height =600 weight = 600>


[參考資料](https://github.com/graphoarty/python-dsa/blob/master/DataStructures/HashTable/HashTable.py)
