流程圖、學習歷程、BST原理
===

BST原理
---

* 簡介

二元搜索樹(Binary Search Tree)是基於二元樹的一種延伸，二元搜索樹的應用範圍很廣，可以利用在搜索、排序和提供資料集合基本結構，發展其他資料結構，所以也是重要的資料結構之一。

* 定義

    * 左子樹不為空，則左子樹的所有節點的鍵值(Key)小於根節點的鍵值。  --> `root.left < root`
    * 右子樹不為空，則右子樹的所有節點的鍵值(Key)大於根節點的鍵值。  --> `root.right > root`
    * 左右子樹也都是二元搜索樹。
    * 節點不會有重複的鍵值。  (但這次作業有)
    
這個定義是樹中的節點都具有Key-value pair情況，有時候可能會其他變化：

沒有鍵值，而用值(Value)來比較。 (像這次作業)

允許重複的資料，此時會出現等於的情況，則將定義1.改成小於等於或者定義2.改成大於等於。 (像這次作業把等於的放到`root.left`)

```py
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
```

流程圖、學習歷程
---

search
---

[參考資料 : youtube頻道](https://www.youtube.com/channel/UCxP77kNgVfiiG6CXZ5WMuAQ)

`search`是在整棵樹裡面我們要尋找到的數值，如果一開始的`head`是一個空值的話那根本找不到東西，所以false

確認`head`不是空值後我們就開始尋找要找的數，我們設一個當前值`root.val`，如果`root.val`等於我們要找的數，那就是正確的

如果`root.val`大於等於我們要找的數且`root.left`(當前數的左邊child)不是空值，那接下來的`root.val`值改為`root.left`值

如果`root.val`小於等於我們要找的數且root.right(當前數的右邊child)不是空值，那接下來的`root.val`值改為`root.right`值

然後不斷重複直到 `root.val=我們要找的數`， return True // 如果找不到，return False

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

首先我們`insert`當然是從樹的頭頭開始，我們先設定`root is None` ，然後直接填入數字

接著再寫 `root != None` 的時候，這個時候填入的值與比較的root會有兩種可能

* `root.val >= val`  ---> 按照規定我們把小的放到左邊，如果 `root.left !=None` ，我們就把`root.left`當成`root.val`再丟到recursive再做一次直到可以直接填入為止

* `root.val <  val  ---> 按照規定我們把大的放到右邊，右邊也和左邊概念相同，只是方向相反而已

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


delete
---

[參考資料 : youtube影片](https://www.youtube.com/watch?v=gcULXE7ViZw)

[參考資料 : youtube頻道](https://www.youtube.com/channel/UCxP77kNgVfiiG6CXZ5WMuAQ)

delete也花了我非常多時間，但其實還算簡單只是我想不到方法做而已

在網路上看影片學習delete是怎麼運作時，學得很快，也很順利寫出程式碼

直到用助教的測值執行時，發現重複的值我沒辦法一次刪掉，因為這個問題卡了好久

如圖 

<img src = "https://github.com/06170230/lulu/blob/master/image/delete.jpg" >

詢問其他同學後，他們告訴我可以利用`search`，找尋我要`delete`的`target`

如果我做完`delete`後還能夠`search`到這個`target`的話，代表這棵樹裡有重複值還沒被刪掉

這個時候我就寫了一個while迴圈，如果還能`search`到我`delete`的`target`，那就再做一次

直到`search(root,target) != True`時，代表`target`值都刪光了，那我們才是真的完成這個`delete`

* 我自己覺得delete最重要的幾個部分

    * 刪除重複值

    * 不同child數量 0、1、2 刪法都不同 

    * 2個child delete 找左邊最大or右邊最小

```py
    def minRightNode(self, root):
        if root.left is None:
            return root
        else:
            return self.minRightNode(root.left)

    def delete(self, root, target):       
        while self.search(root,target) is True:

            if target < root.val:
                root.left = self.delete(root.left, target)

            elif target > root.val:
                  root.right = self.delete(root.right, target)
                  
            else:
                    # 0child or 1child
                if root.left is None:
                    child = root.right
                    root = None
                    return child

                elif root.right is None:
                    child = root.left
                    root = None
                    return child

                elif root.right is None and root.left is None:
                    return None

                     
                    # 我要找右邊最小
                child = self.minRightNode(root.right)

                    
                root.val = child.val

                   
                root.right = self.delete(root.right, child.val)
                
            self.delete(root,target)
            
        else:
            return

```

* 0 child
    * 1 child
        * 2child

<img src = "https://github.com/06170230/lulu/blob/master/image/delete流程圖.jpg"  height =750 weight = 750>



modify
---

[參考資料](https://www.geeksforgeeks.org/how-to-implement-decrease-key-or-change-key-in-binary-search-tree/)

我覺得一般的modify其實很簡單，就只是把`delete`跟`insert`依照我們要提取出來的數和輸入進去的數，重新再做一次而已

但困擾我很久的是，到底該怎麼做才能夠讓binary search tree 的整個長度不會改變

我實在是想不到好方法，不過交作業的時間到了，之後會好好思考一下再重新修改我的程式碼

```py
    def modify (self,root,target,new_val):
        root = self.delete(root,target)
        root = self.insert(root,new_val)
        return root
```
