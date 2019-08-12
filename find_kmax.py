# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:19:32 2019

@author: 10539
"""

def find_kmax(nums,k):
    rec=[]
    rec=nums[0:k]
    rec.sort()
    for i in range(k,len(nums)):
        if nums[i]>rec[0]:
            rec[0]=nums[i]
            temp=0
            for j in range(1,k):
                if rec[temp]>rec[j]:
                    temp=j
            rec[temp],rec[0]=rec[0],rec[temp]
    return rec[0]
a=[1,2,3,4,5,6,7]
print(find_kmax(a,2))

                    