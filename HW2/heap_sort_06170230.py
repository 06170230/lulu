#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Solution(object):
     
    def heap_sort(self, nums):
        size = len(nums) 
        self.heapify(nums, size)
        end = size-1
        while(end > 0):
            self.swap(nums, 0, end)
            self.siftdown(nums, 0, end)
            end = end-1
        return nums
            
    def swap(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i] 
        
  
    
    def siftdown(self,nums, i, size):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left <= size-1 and nums[left] > nums[i]:
            largest = left
        if right <= size-1 and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            self.swap(nums, i, largest)
            self.siftdown(nums, largest, size)
        
        
    def heapify(self,nums, size):
        p = (size//2)-1
        while p>=0:
            self.siftdown(nums, p, size)
            p = p-1
            
output=Solution().heap_sort([6,2,4,9,1,5,8])
output
    


# In[ ]:




