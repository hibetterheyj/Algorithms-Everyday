# -*- coding: utf-8 -*-
"""
1342. Number of Steps to Reduce a Number to Zero
"""

# method1
class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num>0:
            if num%2==0:
                num = num/2
            else:
                num -= 1
            step += 1
        return step

if __name__ == '__main__':
    s=Solution()
    step = s.numberOfSteps(15)
    print(step)