```py
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None
```
search
---

search是在整棵樹裡面我們要尋找到的數值，如果一開始的head是一個空值的話那根本找不到東西，所以false

確認head不是空值後我們就開始尋找要找的數，我們設一個當前值cur.val，如果cur.val等於我們要找的數，那就是正確的

如果cur.val大於等於我們要找的數且cur.left(當前數的左邊child)不是空值，那接下來的cur.val值改為cur.left值

如果cur.val小於等於我們要找的數且cur.right(當前數的右邊child)不是空值，那接下來的cur.val值改為cur.right值

然後不斷重複直到 cur.val=我們要找的數，return True // 如果找不到，return False

```py
class BinaryTree:
    
    def __init__(self):
        self.head = Node(None)
        
    def search(self, target):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, target)

    def __search_node(self, cur, target):
        if cur.val == target:
            return True
        else:
            if cur.val >= target:
                if cur.left is not None:
                    return self.__search_node(cur.left, target)
                else:
                    return False
            else: 
                if cur.right is not None:
                    return self.__search_node(cur.right, target)
                else:
                    return False
   
