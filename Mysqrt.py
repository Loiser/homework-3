# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:27:47 2019

@author: 10539
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or  x==2 or x==3:return 1
        h=x//2
        start=0
        while h>0:
            if (start+h)**2<=x and (start+1+h)**2>x:return start+h
            elif (start+h)**2>x:
                h=(h//2)+1
            else:
                start=start+h
                h=(h//2)+1
        return start
ll=Solution()
print(ll.mySqrt(45))
    