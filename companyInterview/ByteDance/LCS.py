# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:16:34 2020

@author: HYJ
最长公共子序列：https://blog.csdn.net/ggdhs/article/details/90713154
"""
class Solution:
    def LCS(self, strA, strB):
        lenA = len(strA)
        lenB = len(strB)
        if lenA==0 or lenB==0:
            return 0
        res = [[0]*(lenB+1) for _ in range(lenA+1)]
        for i in range(1,lenA+1):
            for j in range(1,lenB+1):
                if strA[i-1] == strB[j-1]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i][j-1],res[i-1][j])
        return res[-1][-1]

s = Solution()
strA = 'gegega'
strB = 'btdrgseg'
print(s.LCS(strA, strB))

            