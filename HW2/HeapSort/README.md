####HeapSort 做法、思考方式、程式碼、流程圖####
===

1.利用的方法 
---
* 堆積排序(Heap Sort)演算法是利用完全二元樹(Complete Binary Tree)，也就是堆積(Heap)結構來完成排序的演算法
* 堆積排序法的概念 :

堆積排序有法兩個大步驟，第一個是把要排序的陣列製作成「最小堆積」(Min Heap)或是「最大堆積」(Max Heap)。如果要將陣列遞增排序的話就使用最大堆積；如果要遞減排序的話就使用最小堆積。這次我是利用最大堆積的方法來做。

[資料來源](https://magiclen.org/heap-sort/)

2.做法
----------
因為自己連heapsort的運作都不了解，所以上網看了一下關於heapsort的影片介紹

[影片連結1/2](https://www.youtube.com/watch?v=S15YazRsjIE&feature=youtu.be)

[影片連結2/2](https://www.youtube.com/watch?v=DO8Vs-sd4Bo)

* 看完影片後開始自己做做看然後在第一部份就馬上卡關了，卡關的點首先要先定義一個變數交換的方式

------>為了後面heaptree移動各個變向

```py
    def swap(list,i,j):
        list[i],list[j]=list[j],list[i] 
```

* 完成以後再定義heaptree裡數字變換的方式

list[6,2,4,9,1,5,8]

若 i=0 --- left = 1 , right = 2

i = 0 對應list裡的 "6"

left = 1 對應list裡的 "2"

right = 2 對應list裡的 "4"

6最大  ----> largest = i ，heaptree不動，但如果left或right之中有比 i 更大且最大的數，就會進行交換，i = largest則不動

```py
    size = len(list)  
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

* 接著找尋binarytree裡面的副節點，從最後一個副節點開始，找出3個一組的largest一路推下去，直到整組數字最大的被放在最上方

這時我們才會得到最大堆積的heaptree

```py
    def heapify(list, size):
        p = (size//2)-1
        while p>=0:
            siftdown(list, p, size)
            p = p-1
```
<img src = "https://github.com/06170230/lulu/blob/master/image/heapify.jpg" height =250 weight = 500>

* 定義完heapify得到最大堆積的heaptree後，我們把頂端最大的數list[0] 移至end處，size也要-1 因為我們不會再去動end處的東西了，接著重複上面所有動作

heaptree最大堆積的largest放到end處後，再繼續做比較把下一個largest放置最上方，然後再移到end處，直到沒有任何數可以移置end，就完成了

```py
    heapify(list, size)
    end = size-1
    while(end > 0):
        swap(list, 0, end)
        siftdown(list, 0, end)
        end = end-1
```

3.完整程式碼
-----
```py
def heapsort(list):
    

    def swap(list,i,j):
        list[i],list[j]=list[j],list[i] 
        
    size = len(list)  
    
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
        
        
    def heapify(list, size):
        p = (size//2)-1
        while p>=0:
            siftdown(list, p, size)
            p = p-1


    heapify(list, size)
    end = size-1
    while(end > 0):
        swap(list, 0, end)
        siftdown(list, 0, end)
        end = end-1

list = [6,2,4,9,1,5,8]
heapsort(list)
print(list)
```
