# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:35:08 2019

@author: 10539
"""

def choose_sort(nums):
    for i in range(len(nums)-1):
        temp=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[temp]: #降序把<换成>
                temp=j
        nums[temp],nums[i]=nums[i],nums[temp]
    return nums
if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(choose_sort(a))

            