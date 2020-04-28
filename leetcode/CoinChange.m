%% 题目描述
%{
You are given coins of different denominations and a total amount of money?
amount. Write a function to compute the fewest number of coins that you
need to make up that amount. If that amount of money cannot be made up
by any combination of the coins, return?`-1`.

示例：
    **Example 1:**
    ```
    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
    ```

    **Example 2:**
    ```
    Input: coins = [2], amount = 3
    Output: -1
    ```

**Note**:You may assume that you have an infinite number of each kind of coin.
%}

%% 代码
clc;clear;close all;
% test case I
coins = [1, 2, 5];amount = 11;
res = coinChange(coins, amount);
disp(res)
% % test case II
coins = [2]; amount = 3;
res = coinChange(coins, amount);
disp(res)

function res = coinChange(coins, amount)
dp = ones(amount+1,1)*inf;
% case0, index=0+1=1
dp(1) = 0;
for step = 1:amount
    for j = 1:numel(coins)
        if coins(j) <= step
            % case_{step}, index={step}+1={step+1}
            dp(step+1) = min(dp(step+1), dp(step+1-coins(j))+1);
        end
    end
end
if dp(amount+1) > amount
    res = -1;
else
    res = dp(amount+1);
end
end