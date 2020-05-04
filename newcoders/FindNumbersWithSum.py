# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:17:33 2020

@author: HYJ
"""

class bruteSolution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        for i in range(len(array)):
            for j in range(len(array)-1, i, -1):
                if array[i] + array[j] == tsum:
                    return [array[i], array[j]]
        return []
    
class sliceSolution:
    def FindNumbersWithSum(self, array, tsum):
        for i in range(len(array)):
            if tsum-array[i] in array[i+1:]:
                # list.index(target, beg, end) 表示从i+1位开始索引
                target = array.index(tsum-array[i], i+1)
                return [array[i], array[target]]
        return []

# https://blog.csdn.net/weixin_44026955/article/details/84921885
# 原方法无法计算出最小的那一对
class hashSolution(object):
    def twoSum(self, array, tsum):
        hashMap = {}
        for i, num in enumerate(array):
            # 感觉得先构造map，词典 key 对应的 val 是他的索引
            hashMap[num] = i
        for i, num in enumerate(array):
            if tsum-num in hashMap:
                target = hashMap[tsum-num]
                return [array[i], array[target]]
        return []

if __name__ == '__main__':
    nums = [2,7,11,16]
    target = 18
    s = hashSolution()
    print(s.twoSum(nums,target))