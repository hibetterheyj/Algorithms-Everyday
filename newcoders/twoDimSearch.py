# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:16:05 2020

@author: HYJ
二维数组查找
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array)
        cols = len(array[0])
        testRow = 0
        testCol = cols - 1
        while testRow < rows and testCol >= 0:
            if array[testRow][testCol] == target:
                return True
            elif array[testRow][testCol] > target:
                testCol -= 1
            else:
                testRow += 1
        return False
    
if __name__ == '__main__':
    target = 6
    array = [[1,2,4,5], [1,4,5,7], [3,4,7,9]]
    s = Solution()
    print(s.Find(target, array))