## QuickSort想法 ##
自己先在紙上想想看

![image](https://github.com/06170230/lulu/blob/master/image/quicksort.jpg)

## QuickSort程式碼##

![image](https://github.com/06170230/lulu/blob/master/image/quicksort%E7%A8%8B%E5%BC%8F%E7%A2%BC.PNG)

先定義一個quick_sort迴圈
依照取基準點並分類成較大、較小兩種，設置兩個資料smaller[]、bigger[]

當list裡的變數只有一個時直接返還
若不只一個時，我們先設定list裡的第一個數值為基準點
若list裡的數 > key值，放入bigger
            < key值，放入smaller
假設list = [3,5,7,4,1]

第一層 :
key值為3
bigger = [5,7,4]
smaller = [1]

第二層 : 
key值為5
bigger = [7]
smaller = [4]

第一層分層完結果為 [1,3,5,7,4]
第二層分層完結果為 [1,3,4,5,7]

## QuickSort流程圖 ##
<img src = "https://github.com/06170230/lulu/blob/master/image/流程圖.jpg" height =500 weight = 500>
