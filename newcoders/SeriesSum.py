# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:36:59 2020

@author: HYJ
剑指offer中不适用加减乘除，for循环实现数列和
"""

class Solution:
    def SeriesSum(self, n):
        return n and (n + self.SeriesSum(n-1))
    def Fib(self, n):
        if n == 0 or n == 1:
            return 1
        return n and (self.Fib(n-2) + self.Fib(n-1))
    def FibLoop(self, n):
        a, b = 0,1
        for i in range(n+1):
            a, b = b, a+b
        return a
    
if __name__ == '__main__':
    n = 10
    s = Solution()
#    print(s.SeriesSum(3))
#    print(s.Fib(n))
    print(s.FibLoop(n))
    
    