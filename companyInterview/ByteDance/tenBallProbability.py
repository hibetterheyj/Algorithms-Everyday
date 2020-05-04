# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 17:12:50 2020

@author: HYJ

10个小球，随机分到12个盒子里，求恰好10个盒子都为空的概率。
"""

import random
test = 1000000
succ = 0
for i in range(test):
    bucket = [0] * 12
    for i in range(10):
        rnd = random.randint(0,11)
        bucket[rnd] += 1
    times = 0
    for i in range(12):
        if bucket[i] == 0:
            times += 1
    if times == 10:
        succ += 1
    
print("%.10f" % (succ/test))