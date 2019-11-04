####MergeSort 做法、思考方式、程式碼、流程圖####
===

1.利用的方法 Divide-and-Conquer
---
Divide and conquer中文翻作分治法，概念如字面上的意義，將問題先切分成小問題後再解決，再將結果合併求出原始問題的答案。

提升程式效率，例如歸併排序(Merge Sort)讓排序速度提升。

* 步驟:

   * 分解：將原問題分解為若干個規模較小，相對獨立，與原問題形式相同的子問題。

   * 解決：若子問題規模較小且易於解決時，則直接解。否則，遞歸地解決各子問題。

   * 合併：將各子問題的解合併為原問題的解。

[資料來源](https://emn178.pixnet.net/blog/post/87739443-divide-and-conquer)

2.做法
----------
一開始真的不會做雖然有頭緒但想不到要怎麼用程式碼呈現所以上網參考了一下其他人的程式碼
   
先定義mergeSort

然後把資料分成三大部分----分別是  mid(中點)、left(左半部)、right(右半部)

接著設三個變數 i、j、a 如果 i、j 沒有超過left跟right的長度就可以比較i、j

建立一個迴圈

假如left[i]<=right[j]，就把left[i]加進list[a]之中
i輪到下一個 ---> i=i+1

如果right[j]<=left[i]，就把right[j]加進list[a]之中
j輪到下一個 ---> j=j+1

```py
def mergeSort(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        i=0
        j=0
        a=0
        
  # 下面兩段很重要一開始忘了呼叫mergeSort就跑迴圈了根本沒有意義! ###
        
        mergeSort(left)
        mergeSort(right)   
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[a]=left[i]
                i=i+1
                a=a+1
            else:
                list[a]=right[j]
                j=j+1
                a=a+1
list=[1,5,9,7,2,6,15,20,10,11]
mergeSort(list)
list
```
以上是我第一次做的程式碼，但跑出來的結果是 [1, 2, 2, 2, 2, 6, 15, 20, 10, 11]

但是我自己想了好久實在是想不到我到底漏了甚麼，為什麼結果跟我想像的不一樣

後來發現如果照我上面打的程式碼的想法在書上寫一次

★發現資料沒有辦法完全填完 i、j 都比完以後還剩下最後一個最大的值，但我的程式碼還沒有把它加進去★

所以當"i""j"其中一邊小於"left"或"right"，代表有一邊已經填完了，只要再加上剩下"i"或"j"就能完成

我們加上這段程式碼

```py
        while i < len(left):
            list[a]=left[i]
            i=i+1
            a=a+1

        while j < len(right):
            list[a]=right[j]
            j=j+1
            a=a+1
```
結果為[1, 2, 5, 6, 7, 9, 10, 11, 15, 20]

成功了！

完整的程式碼貼在這邊

```py
def mergeSort(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        i=0
        j=0
        a=0
        # 下面兩段很重要一開始忘了呼叫mergeSort就跑迴圈了根本沒有意義! #
        mergeSort(left)
        mergeSort(right)
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[a]=left[i]
                i=i+1
                a=a+1
            else:
                list[a]=right[j]
                j=j+1
                a=a+1
        #下面這兩個while很重要，如果沒有加上來i、j比大小結束後剩下的最大值就沒有被加上來            
        while i < len(left):
            list[a]=left[i]
            i=i+1
            a=a+1

        while j < len(right):
            list[a]=right[j]
            j=j+1
            a=a+1
                
list=[1,5,9,7,2,6,15,20,10,11]
mergeSort(list)
list
```
[程式碼參考處](https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html)

3.流程圖
---
<img src = "https://github.com/06170230/lulu/blob/master/image/mergesort.jpg" height =750 weight = 750>
