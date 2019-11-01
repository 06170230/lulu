實作概念
把整個linked-list的實作分成兩個類別（class），一個是包含了資料及指標兩個屬性的節點（class ListNode），
另一個則是定義出各種資料結構操作的list本身（class SingleLinkedList）。
``` py
class ListNode:
  def __init__(self, data): 
    # store data
    self.data = data
    # store the reference (next item)
    self.next = None
    return
    
    在建立一個節點時，需要傳入一個data的值，並且指標預設是指向None的。
    
class SingleLinkedList:
  def __init__(self): 
    self.head = None
    self.tail = None
    return
    
    ```
在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟tail兩個屬性。當我們加入一個新的節點時：
若list本身還沒有任何節點，則head以及tail都會變成新的結點
若list已經包含有其他節點，則新加入的節點變成新的tail（本來的tail指向新的節點）。
