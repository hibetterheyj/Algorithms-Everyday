# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:11:35 2020

@author: HYJ

计算矩阵连通域个数

rewrite from https://blog.csdn.net/github_29705847/article/details/100523699
https://blog.csdn.net/wphkadn/article/details/100125148
"""


#import numpy as np
#import matplotlib.pyplot as plt
# 
# 
#class solution:
#    def __init__(self,im):
#        self.im=im
#        m,n=im.shape
#        self.mask=[[0 for _ in range(n)] for _ in range(m)]
#    def isValid(self,i,j,mask,im):
#        m,n=im.shape
#        return i>=0 and i<m and j>=0 and j<n and mask[i][j]==0 and im[i][j]==1
# 
#    def add(self,i,j,mask,im,q):
#        if self.isValid(i,j,mask,im):
#            q.append([i,j])
#            self.mask[i][j]=1
# 
#    def bsfsolver(self):
#        # 首先得到整个方程的尺寸
#        m,n=self.im.shape
#        # 结果为空
#        res=[]
#        # 开始诸葛遍历
#        for i in range(m):
#            for j in range(n):
#                # 这个跳过本次循环的操作没看懂
#                if self.mask[i][j]==1 or self.im[i][j]==0:
#                    continue
#                P,Q=list(),list()
#                P.append([i,j])
#                # 这个mask应该就是visit的功能
#                self.mask[i][j]=1
#                while P:
#                    temp=P.pop(0)
#                    Q.append(temp)
#                    self.add(temp[0]-1,temp[1],self.mask,im,P)
#                    self.add(temp[0]+1,temp[1],self.mask,im,P)
#                    self.add(temp[0],temp[1]-1,self.mask,im,P)
#                    self.add(temp[0],temp[1]+1,self.mask,im,P)
#                res.append(Q)
#        # 输出len(res)即可得到个数！
#        return res
# 
# 
#if __name__ =='__main__':
#    im=np.zeros(shape=(120,120))
#    im[1:10,6:20]=1
#    im[7:20,15:50]=1
#    im[26:40,25:60]=1
#    im[45:80,66:90]=1
# 
#    s=solution(im)
#    res=s.bsfsolver()
# 
#    cen=[]
#    for i in range(len(res)):
#        x=res[i]
#        cenx=[x_[0] for x_ in x]
#        ceny=[x_[1] for x_ in x]
#        cen.append([sum(cenx)/len(cenx),sum(ceny)/len(ceny)])
# 
#    plt.figure(0)
#    plt.imshow(im)
# 
#    for i,c in enumerate(cen):
#        plt.text(c[1],c[0],str(i+1),fontsize=11)
#    plt.show()
#    print(len(res))
    
########################################
#################简化版
########################################
class Solution:
    def bfsSolver(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        visited = [[0]*cols for _ in range(rows)]
        def addornot(i,j,visited,mat,mem,rows,cols):
            if i>=0 and j>=0 and i<rows and j<cols and visited[i][j]==0 and mat[i][j]==1:
                mem.append([i,j])
                visited[i][j]=1
            return visited, mem
        P, Q = list(), list()
        res = []
        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==1 or mat[i][j]==0:
                    continue
                P.append([i,j])
                while P:
                    temp = P.pop(0)
                    Q.append(temp)
                    visited, P = addornot(temp[0],temp[1]+1,visited,mat,P,rows,cols)
                    visited, P = addornot(temp[0],temp[1]-1,visited,mat,P,rows,cols)
                    visited, P = addornot(temp[0]-1,temp[1],visited,mat,P,rows,cols)
                    visited, P = addornot(temp[0]+1,temp[1],visited,mat,P,rows,cols)
                res.append(Q)
        return len(res)

if __name__ == '__main__':
    mat = [[1,1,1,1,1],
           [1,0,0,0,0],
           [1,1,0,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0]]
    s = Solution()
    print(s.bfsSolver(mat))