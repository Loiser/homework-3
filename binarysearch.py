# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:24:35 2019

@author: 10539
"""
#默认nums从小到大排列
def binarysearch(target,nums,start,end):
    l=end-start+1
    if l<1:return False
    h=l//2
    if nums[start+h]==target:return start+h
    elif nums[start+h]>target:return binarysearch(target,nums,start,start+h-1)
    else:return binarysearch(target,nums,start+h+1,end)
a=[1,3,4,7,9,22,66]
print(binarysearch(1,a,0,len(a)-1))