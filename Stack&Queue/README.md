Stack
===

* 從後面取

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

* 從前面取

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
