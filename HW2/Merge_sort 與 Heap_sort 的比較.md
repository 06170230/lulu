Merge Sort(合併排序法) VS Heap Sort(堆積排序法)
===

Merge Sort
---

Merge Sort屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。

Heap Sort
---

將資料轉換為 heap 資料結構（遞增排序用 max-heap, 遞減排序選擇 min-heap）。逐步取出最大／最小值，並與最後一個元素置換，直到 heap 中剩最後一個未排序的資料。


* Heap Sort 與 Merge Sort 不同處
  * Heap Sort是「原地排序」：不需額外花費儲存空間來排序 //   Merge Sort 會需要建立新的空間
  * Merge Sort 處理大筆資料時速度較 Heap Sort 來的快
  * Heap Sort 會根據數據的不同隨機遍歷 // Merge Sort 的每次遍歷都會按照順序

遍歷的意思 : 所謂遍歷(Traversal)，是指沿著某條探索路線，依次對樹（或圖）中每個節點做訪問。


參考資料
---

* http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html
* http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html#hs
