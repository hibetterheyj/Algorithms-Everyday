%% 题目描述
%{
Given a valid (IPv4) IP?`address`, return a defanged version of that IP address.
A?*defanged?IP address*?replaces every period?`"."`?with?`"[.]"`.

示例：
    **Example 1:**
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

    
    **Example 2:**
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"
    
约束条件：
**Constraints:**
- 1 <= candies <= 10^9
- 1 <= num_people <= 1000
%}

%% TODO
% 增加约束条件判断

%% 代码
clc;clear;close all;

address1 = "255.100.50.0"
res = defangIPaddr(address1);
disp(res)

address2 = "1.1.1.1"
res = defangIPaddr(address2);
disp(res)


function newAddr = defangIPaddr(address)
    newAddr = strrep(address, '.', '[.]');
end