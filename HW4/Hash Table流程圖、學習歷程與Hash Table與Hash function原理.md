Hash Table流程圖、學習歷程與Hash Table與Hash function原理
===

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

<img src = "https://github.com/06170230/lulu/blob/master/image/hashtable_contains.jpg" height =700 weight = 700>
