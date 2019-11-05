####HeapSort 做法、思考方式、程式碼、流程圖####
===

1.利用的方法 
---
* 堆積排序(Heap Sort)演算法是利用完全二元樹(Complete Binary Tree)，也就是堆積(Heap)結構來完成排序的演算法
* 堆積排序法的概念 :

堆積排序有法兩個大步驟，第一個是把要排序的陣列製作成「最小堆積」(Min Heap)或是「最大堆積」(Max Heap)。如果要將陣列遞增排序的話就使用最大堆積；如果要遞減排序的話就使用最小堆積。這次我是利用最小堆積的方法來做。

[資料來源](https://magiclen.org/heap-sort/)

2.做法
----------
因為自己連heapsort的運作都不了解，所以上網看了一下關於heapsort的影片介紹

[影片連結1/2](https://www.youtube.com/watch?v=S15YazRsjIE&feature=youtu.be)

[影片連結2/2](https://www.youtube.com/watch?v=DO8Vs-sd4Bo)

看完影片後開始自己做做看然後在第一部份就馬上卡關了，卡關的點首先要先定義一個變數交換的方式

------>為了後面heaptree移動各個變向

```py
    def swap(list,i,j):
        list[i],list[j]=list[j],list[i] 
```

完成以後再定義heaptree裡數字變換的方式

list[6,2,4,9,1,5,8]

若 i=0 --- left = 1 , right = 2

i = 0 對應list裡的 "6"

left = 1 對應list裡的 "2"

right = 2 對應list裡的 "4"

6最大  ----> largest = i ，heaptree不動，但如果left或right之中有比 i 更大且最大的數，就會進行交換，i = largest則不動

```py
    def siftdown(list, i, size):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left <= size-1 and list[left] > list[i]:
            largest = left
        if right <= size-1 and list[right] > list[largest]:
            largest = right
        if largest != i:
            swap(list, i, largest)
            siftdown(list, largest, size)
```
