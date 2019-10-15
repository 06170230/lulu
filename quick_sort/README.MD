## QuickSort想法 ##
先定義一個quick_sort迴圈
依照取基準點並分類成較大、較小兩種，先設置兩筆資料smaller[]、bigger[]

當list裡的資料只有一個時直接返還
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
![image](https://github.com/06170230/lulu/blob/master/image/quicksort.jpg)
## QuickSort程式碼##
In [23]:


def quick_sort(list): 
    smaller = []
    bigger = []
    
    if len(list) <= 1:
        return list
​
    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                smaller.append(i)
            elif i > key: #比key值大的數
                bigger.append(i)
         
    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)
    return smaller + [key] + bigger



In [24]:


list = [3,5,7,4,1]



In [25]:


quick_sort(list)


Out[25]:
[1, 3, 4, 5, 7]



