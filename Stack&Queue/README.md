Stack
===

Stack 必須有的功能
---

* Push(data):把資料放進Stack。把書放進箱子。

* Pop:把「最上面」的資料從Stack中移除。把箱子中「最上面」的書拿出來。

* Top:回傳「最上面」的資料。確認箱子「最上面」的是哪本書。

* IsEmpty:確認Stack裡是否有資料。確認箱子裡面有沒有書。

* getSize:回傳Stack裡的資料個數。記錄目前箱子已經裝了多少本書。

```py
class Stack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
    def IsEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def getSize(self):
        return len(self.stack)
```


Queue
===

Queue 必須有的功能
---

* Push(data):把資料從Queue的「後面」放進Queue,並更新成新的back.

* Pop:把front所指向的資料從Queue中移除,並更新front。從Queue刪除資料又稱為dequeue.

* getFront:回傳front所指向的資料。

* getBack:回傳back所指向的資料。

* IsEmpty:確認Queue裡是否有資料。

* getSize:回傳Queue裡的資料個數。

```py
class Queue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)
        
    def getFront(self) -> int:
        return self.queue[0]
    
    def getBack(self):
        return self.queue[-1]
        
    def IsEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def getSize(self):
        return len(self.queue)
```
