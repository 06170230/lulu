#!/usr/bin/env python
# coding: utf-8

# In[5]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self, root, val):
    
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if root.val >= val:
                if root.left != None:
                    root.left = self.insert(root.left, val)                    
                else:
                    root.left = TreeNode(val)
                    return root.left
                
            elif root.val < val:
                if root.right != None:
                    root.right = self.insert(root.right, val)
                    
                else:
                    root.right = TreeNode(val)    
                    return root.right
###
    def search(self, root, target):
        if root is None:
            return None
        else:
            if root.val == target:
                return root
            else:
                if root.val > target:
                    if root.left is not None:
                        return self.search(root.left, target)
                    else:
                        return None
                elif root.val < target:   
                    if root.right is not None:
                        return self.search(root.right, target)
                    else:
                        return None
###                    
    def search_delete(self, root, target):
        if root is None:
            return None
        else:
            if root.val == target:
                return True
            else:
                if root.val > target:
                    if root.left is not None:
                        return self.search_delete(root.left, target)
                    else:
                        return None
                elif root.val < target:   
                    if root.right is not None:
                        return self.search_delete(root.right, target)
                    else:
                        return None
    def minRightNode(self,root): 
        
        while(root.left is not None): 
            root = root.left  
  
        return root  
    
    def delete(self, root, target):
        
        while self.search_delete(root,target) is True:
            
            if target < root.val:
                root.left = self.delete(root.left, target)
                
            elif target > root.val:
                root.right = self.delete(root.right, target)
                
            else:
                    # 0child or 1child
                if root.left is None:
                    child = root.right
                    root = None
                    return child

                elif root.right is None:
                    child = root.left
                    root = None
                    return child

                elif root.right is None and root.left is None:
                    return 

                    # 我要找右邊最小
                child = self.minRightNode(root.right)
                root.val = child.val
                root.right = self.delete(root.right, child.val)
            self.delete(root,target)
        else:
            return root
 ###       
    def modify(self,root,target,new_val):
        if target != new_val:       
            self.insert(root,new_val)
            return self.delete(root,target)
        else:
            return root

