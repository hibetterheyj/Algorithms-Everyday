# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/github_29705847/article/details/100523699
leetcode 200. Number of Islands
"""

import numpy as np
import matplotlib.pyplot as plt
 
 
class solution:
    def __init__(self,im):
        self.im=im
        m,n=im.shape
        self.mask=[[0 for _ in range(n)] for _ in range(m)]
    def isValid(self,i,j,mask,im):
        m,n=im.shape
        return i>=0 and i<m and j>=0 and j<n and mask[i][j]==0 and im[i][j]==1
 
    def add(self,i,j,mask,im,q):
        if self.isValid(i,j,mask,im):
            q.append([i,j])
            self.mask[i][j]=1
 
    def bsfsolver(self):
        m,n=self.im.shape
        res=[]
        for i in range(m):
            for j in range(n):
                if self.mask[i][j]==1 or self.im[i][j]==0:
                    continue
                P,Q=list(),list()
                P.append([i,j])
                self.mask[i][j]=1
                while P:
                    temp=P.pop(0)
                    Q.append(temp)
                    self.add(temp[0]-1,temp[1],self.mask,im,P)
                    self.add(temp[0]+1,temp[1],self.mask,im,P)
                    self.add(temp[0],temp[1]-1,self.mask,im,P)
                    self.add(temp[0],temp[1]+1,self.mask,im,P)
                res.append(Q)
        return res
 
 
if __name__ =='__main__':
    im=np.zeros(shape=(120,120))
    im[1:10,6:20]=1
    im[7:20,15:50]=1
    im[26:40,25:60]=1
    im[45:80,66:90]=1
 
    s=solution(im)
    res=s.bsfsolver()
 
    cen=[]
    for i in range(len(res)):
        x=res[i]
        cenx=[x_[0] for x_ in x]
        ceny=[x_[1] for x_ in x]
        cen.append([sum(cenx)/len(cenx),sum(ceny)/len(ceny)])
 
    plt.figure(0)
    plt.imshow(im)
 
    for i,c in enumerate(cen):
        plt.text(c[1],c[0],str(i+1),fontsize=11)
    plt.show()
    print(len(res))
 
 
