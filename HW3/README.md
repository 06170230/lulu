```py
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class BinaryTree:
    
    def __init__(self):
        self.head = Node(None)
        
    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False
   
