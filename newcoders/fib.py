# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:29:28 2020

@author: HYJ
"""

def fib(n):
    a, b = 0, 1
    while n>0:
        a, b = b, a+b
        n -= 1
    return a

if __name__ == '__main__':
    print(fib(5))