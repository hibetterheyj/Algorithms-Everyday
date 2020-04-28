# -*- coding: utf-8 -*-
"""
55. Jump Game
"""
# Greedy
class Solution1:
    def canJump(self, nums):
        # 避免[0]情况的发生
        if len(nums) == 1:
            return True
        else:
            # 初始化
            reach = nums[0]
            for i in range(0,len(nums)):
                # 在就有可到达最大与当前可到达最大之间进行更新！
                reach = max(reach, i+nums[i])
                # 两种退出条件
                if reach <= i:
                    return False
                if reach >= len(nums)-1:
                    return True
    
# DP!!!
class Solution2:
    def canJump(self, nums):
        dp = nums[0]
        for i in range(0,len(nums)):
            if dp > 0:
                dp -= 1
                dp = max(dp,nums[i])
            else:
                return False
        return True
    
if __name__ == '__main__':
    s=Solution1()
    res = s.canJump([3,2,1,0,4])
    print(res)
    res = s.canJump([0,1])
    print(res)
    res = s.canJump([0])
    print(res)