# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:44:27 2019

@author: 10539
"""


def sort(arr,start,end):
    if end == start * 2:
        if arr[start * 2] > arr[start]:
            arr[start * 2], arr[start] = arr[start], arr[start * 2]
    else:
        if end < start * 2 + 1:
            return
        else:
            left = arr[start*2]
            right = arr[start*2+1]
            if left>right and left > arr[start]:
                arr[start * 2 ], arr[start] = arr[start], arr[start * 2 ]
                sort(arr,start*2,end)
            if left<right and right > arr[start]:
                arr[start * 2+1], arr[start] = arr[start], arr[start * 2+1]
                sort(arr, start * 2+1, end)

def heapfiy(arr):
    x = len(arr) - 1
    n = x // 2
    while n > 0:
        # print(n)
        sort(arr, n, x)
        n -= 1


#第一个0是占位用
orignal_list=[0, 74, 73, 59, 72, 64, 69, 43, 36, 70, 61, 40, 16, 47, 67, 17, 31, 19, 24, 14, 20, 48, 5, 7, 3, 78, 84, 92, 97, 98, 99]
#第一次构建最大堆
heapfiy(orignal_list)

x= len(orignal_list) - 1
while x!=1:
    #交换最大的数和最后一个
    orignal_list[1],orignal_list[x]=orignal_list[x],orignal_list[1]
    x-=1
    #由于交换了，不再是最大堆，重新构建最大堆
    n=x//2
    while n>0:
        sort(orignal_list,n,x)
        n-=1


print(orignal_list) 