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


insert
---

[參考資料 : youtube頻道](https://www.youtube.com/channel/UCxP77kNgVfiiG6CXZ5WMuAQ)

[參考資料](https://stackoverflow.com/questions/44742516/binary-search-tree-recursive-insertion-python)

[參考資料](https://stackoverflow.com/questions/45931836/insert-in-binary-search-tree-using-recursion-in-python)

[參考資料](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/)

insert對我來說根本是地獄，我整整花了快三天才解決我的問題，看到參考資料這麼多就知道我有多迷惘了

首先我們insert當然是從樹的頭頭開始，我們先設定"root is None" ，然後直接填入數字

接著再寫 root != None 的時候，這個時候填入的值與比較的root會有兩種可能

* root.val >= val  ---> 按照規定我們把小的放到左邊，如果 root.left !=None ，我們就把root.left當成root.val再丟到recursive再做一次直到可以直接填入為止

* root.val <  val  ---> 按照規定我們把大的放到右邊，右邊也和左邊概念相同，只是方向相反而已

接著來看看我卡住的地方

<img src = "https://github.com/06170230/lulu/blob/master/image/insertwrong.jpg" >

就算這邊沒有加上 root.left = // root.right = 也能跑出結果，而且也有辦法insert到正確位置，但就是沒辦法對上，要好好注意哦!

```py
class Solution(object):
        
    def insert(self, root, val):
    
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if root.val >= val:
                if root.left != None:
                    root.left = self.insert(root.left, val)                    
                else:
                    root.left = TreeNode(val)
                    return root.left
                
            elif root.val < val:
                if root.right != None:
                    root.right = self.insert(root.right, val)
                    
                else:
                    root.right = TreeNode(val)    
                    return root.right
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
Solution().insert(root,4)
Solution().insert(root,4) == root.left.right
```

* 設立 tree

    * insert(root,4)
        
        * 檢查insert(root,4)位置

<img src = "https://github.com/06170230/lulu/blob/master/image/insert.jpg"  height =500 weight = 500>
