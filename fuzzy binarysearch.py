# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:45:06 2019

@author: 10539
"""
#这里对比第一个元素小的数没有考虑
def fuzzy_binarysearch(target,nums,start,end):
    l=end-start+1
    if l<2:return False
    h=l//2
    if nums[start+h-1]<target and nums[start+h]>=target :return start+h
    elif nums[start+h-1]==target :return start+h-1
    elif nums[start+h-1]>target :return fuzzy_binarysearch(target,nums,start,start+h-1)
    else:return fuzzy_binarysearch(target,nums,start+h,end)
a=[1,3,4,7,9,22,66]
print(fuzzy_binarysearch(7,a,0,len(a)-1))