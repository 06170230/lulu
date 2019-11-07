#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution(object):
    def merge_sort(self,nums):
        if len(nums)>1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            i=0
            j=0
            a=0
        # 下面兩段很重要一開始忘了呼叫mergesort就跑迴圈了根本沒有意義! #
            self.merge_sort(left)
            self.merge_sort(right)
        
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[a]=left[i]
                    i=i+1
                    a=a+1
                else:
                    nums[a]=right[j]
                    j=j+1
                    a=a+1
         
        #下面這兩個while很重要，如果沒有加上來i、j比大小結束後剩下的最大值就沒有被加上來            
            while i < len(left) and j == len(right) :
                nums[a]=left[i]
                i=i+1
                a=a+1

            while j < len(right) and i == len(left) :
                nums[a]=right[j]
                j=j+1
                a=a+1
            return nums
        
output=Solution().merge_sort([1,5,9,7,2,6,15,20,10,11])               
output


# In[ ]:




