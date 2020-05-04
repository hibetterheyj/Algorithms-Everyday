# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:31:07 2020

@author: HYJ

广度优先搜索、动态规划
https://blog.csdn.net/weixin_40546602/article/details/88880454
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS宽度优先搜索
        # 先找到所有的0点
        # 从0层开始搜索，与0相连的非0值全部为1
        # 继续搜索1层，与1相连的、未被遍历过的点且非0的点的值置为当前层1+1
        
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        # 构建一个map
        visited = [[0]*n for i in range(m)]
        Q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited[i][j] = 1
                    Q.append([i,j])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        cur_num = 0 
        while Q:
            size = len(Q)
            for _ in range(size):
                x, y = Q.pop(0)
                for i in range(4):
                    newx, newy = x + dx[i], y + dy[i]
                    if newx < 0 or newy < 0 or newx >= m or newy >= n:
                        continue
                    if visited[newx][newy]:
                        continue
                    visited[newx][newy] = 1
                    if matrix[newx][newy] != 0:
                        matrix[newx][newy] = cur_num + 1
                        Q.append([newx,newy])
            cur_num += 1
        return matrix
    
if __name__ == '__main__':
    matrix = [[1,0],[1,1]]
    s = Solution()
    print(s.updateMatrix(matrix))