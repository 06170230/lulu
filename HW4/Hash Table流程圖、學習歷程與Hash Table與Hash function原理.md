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
