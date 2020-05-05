# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:12:11 2020

@author: HYJ

顺时针由外向内打印矩阵
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix:
                matrix = self.rotateMat(matrix)
        return res
        
    def rotateMat(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        newMat = []
        for i in range(cols):
            newLine = []
            for j in range(rows):
                # 关键旋转矩阵需要算好
                newLine.append(matrix[j][cols-i-1])
            newMat.append(newLine)
        return newMat

if __name__ == '__main__':
    # 测试代码
    matrix = [
        [1, 2, 3, 4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9, 8, 7]]
    s = Solution()
    result = s.printMatrix(matrix)
    print(result)