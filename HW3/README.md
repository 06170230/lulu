```py
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
```
search
---

[參考資料 : youtube頻道](https://www.youtube.com/channel/UCxP77kNgVfiiG6CXZ5WMuAQ)

search是在整棵樹裡面我們要尋找到的數值，如果一開始的head是一個空值的話那根本找不到東西，所以false

確認head不是空值後我們就開始尋找要找的數，我們設一個當前值root.val，如果root.val等於我們要找的數，那就是正確的

如果root.val大於等於我們要找的數且root.left(當前數的左邊child)不是空值，那接下來的root.val值改為root.left值

如果root.val小於等於我們要找的數且root.right(當前數的右邊child)不是空值，那接下來的root.val值改為root.right值

然後不斷重複直到 root.val=我們要找的數，return True // 如果找不到，return False

```py
class Solution(object):
    
    def __init__(self):
        self.head = TreeNode(None)      

    
    def search_head(self,target):
        if self.head.val is None:
            return False
        else:
            return self.search(self.head, target)
        
    def search(self, root, target):
        if root.val == target:
            return True
        else:
            if root.val >= target:
                if root.left is not None:
                    return self.search(root.left, target)
                else:
                    return False
            elif root.val < target:   
                if root.right is not None:
                    return self.search(root.right, target)
                else:
                    return False      

                
root = TreeNode(5)
root.right = TreeNode(7)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
```   
<img src = "https://github.com/06170230/lulu/blob/master/image/search.jpg" >

* 找的目標為7 
* 找的目標為8

<img src = "https://github.com/06170230/lulu/blob/master/image/search1.jpg" height =400 weight = 500 >
