1. 利用的方法 Divide-and-Conquer
............
2. 做法

   
先定義mergeSort

然後把資料分成三大部分----分別是  mid(中點)、left(左半部)、right(右半部)

接著設三個變數 i、j、a 如果 i、j 沒有超過left跟right的長度就可以比較i、j

---
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
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[a]=left[i]
                i=i+1
            else:
                list[a]=right[j]
                j=j+1
                a=a+1
list=[1,5,9,7,2,6,15,20,10,11]
mergeSort(list)
list
```
