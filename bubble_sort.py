# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:20:08 2019

@author: 10539
"""

def bubble_sort(nums):
    i=len(nums)-1
    while i>0 :
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        i-=1
    return nums
if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(bubble_sort(a))
