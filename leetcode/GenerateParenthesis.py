# -*- coding: utf-8 -*-
"""
22. Generate Parentheses
"""

class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(prefix, left, right):
            if len(prefix) == 2*n:
                res.append(prefix)
                return
            if left < n:
                # 这里是转到下一种情况，但不是直接输出return
                backtrack(prefix+'(', left+1, right)
            if right < left:
                #与上面同理
                backtrack(prefix+')', left, right+1)
        backtrack('', 0, 0)
        return res
if __name__ == '__main__':
    s=Solution()
    step = s.generateParenthesis(3)
    print(step)