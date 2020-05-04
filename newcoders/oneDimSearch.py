# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:15:55 2020

@author: HYJ
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        n=len(array)
        l=0
        r=n-1
        while l<r:
            mid=(l+r)//2
            if array[mid]>=target:
                # 这一步比较重言，记住是索引mid
                r=mid
            else:
                l=mid+1
        # 找到位置之后再判断
        if array[l]!=target:
            return False
        return True
if __name__ == '__main__':
    s = Solution()
    print(s.Find(4, [1,2,3,4]))