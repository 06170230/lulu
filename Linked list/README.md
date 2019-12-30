實作概念:

把整個linked-list的實作分成兩個類別（class），一個是包含了資料及指標兩個屬性的節點（class Node），
另一個則是定義出各種資料結構操作的list本身（class MyLinkedList）。
``` py
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0


    def get(self, index):  #查詢
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.size == 0:
            return -1
        
        elif index < 0 or index >= self.size:
            return -1
        

        pointer = self.head     
        for i in range(index):
            pointer = pointer.next
        return pointer.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = Node(val)
        
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            
        self.size+=1
   
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = Node(val)
        
        else:
            pointer = self.head
            while pointer.next!=None:
                pointer = pointer.next
            else:
                pointer.next = Node(val)
                
        self.size+=1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = Node(val)
            
        else:
            if index == 0:
                self.addAtHead(val)
                
            elif index == self.size:
                self.addAtTail(val)
                
            elif index < 0 or index >self.size:
                return
            
            else:
                pointer = self.head
                for i in range(index-1):
                    pointer = pointer.next
                node = Node(val)
                node.next = pointer.next
                pointer.next = node
                
        self.size+=1
       

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.size == 0:
            return
        
        if index < 0 or index >= self.size:
            return
        
        else:
            pointer = self.head
            if index == 0:
                self.head = pointer.next
                
            else:
                for i in range(index-1):
                    pointer = pointer.next
                pointer.next = pointer.next.next

        self.size-=1
```
在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟next兩個屬性。當我們加入一個新的節點時：
若list本身還沒有任何節點，則head以及next都會變成新的結點
若list已經包含有其他節點，則新加入的節點變成新的next（本來的next指向新的節點）。
