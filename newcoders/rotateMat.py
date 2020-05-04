# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:54:13 2020

@author: HYJ
"""

class Solution:
    # 顺时针
    def rotataMat(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        newMat = []
        for i in range(cols):
            newRow = []
            for j in range(rows):
                newRow.append(mat[rows-j-1][i])
            # 不要写成 = 模式
            newMat.append(newRow)
        return newMat
    # 顺时针
    def reverseRotataMat(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        newMat = []
        for i in range(cols):
            newRow = []
            for j in range(rows):
                newRow.append(mat[j][cols-1-i])
            newMat.append(newRow)
        return newMat
    # 镜像
    def mirrorMat(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        newMat = []
        for i in range(rows):
            newRow = []
            for j in range(cols):
                newRow.append(mat[i][cols-1-j])
            newMat.append(newRow)
        return newMat
        
    
if __name__ == '__main__':
    mat = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]
    s = Solution()
    print('Rotate the Matrix in 90 degree: {}\n'.format(s.rotataMat(mat)))
    print('Rotate the Matrix in -90 degree: {}\n'.format(s.reverseRotataMat(mat)))
    print('Mirror the Matrix: {}\n'.format(s.mirrorMat(mat)))