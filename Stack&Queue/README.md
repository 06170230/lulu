Stack
===

```py
class Stack:

    def __init__(self):
        self.item = []
        
    def add(self, target):
        self.item.append(target)
    
    def pop(self) -> None:
        self.item.pop(-1)
        
    def top(self) -> int:
        return self.item[-1]
    
    def is_empty(self):
        if len(self.item) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.item)
```


Queue
===

```py
class Queue:

    def __init__(self):
        self.items = []

    def add(self, target):
        self.items.append(target)

    def pop(self):
        self.items.pop(0)

    def print_queue(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
```
