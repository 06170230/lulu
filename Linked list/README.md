實作概念:

把整個linked-list的實作分成兩個類別（class），一個是包含了資料及指標兩個屬性的節點（class ListNode），
另一個則是定義出各種資料結構操作的list本身（class LinkedList）。
``` py
class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print("item does not exist in linked list")

    def removeItem(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
    
```
在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟next兩個屬性。當我們加入一個新的節點時：
若list本身還沒有任何節點，則head以及next都會變成新的結點
若list已經包含有其他節點，則新加入的節點變成新的next（本來的next指向新的節點）。
