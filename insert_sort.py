# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:00:53 2019

@author: 10539
"""

def insert_sort(nums):
    for i in range(1,len(nums)):
        j=i-1
        t=nums[i]
        while(j>=0 and t<nums[j]):
            nums[j+1],nums[j] = nums[j],nums[j+1]
            j-=1
    return  nums
if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(insert_sort(a))
