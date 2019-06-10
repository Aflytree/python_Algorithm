#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2019 Lynxi Ltd. All rights reserved.
#   
#   @name          ：profit.py
#   @author        ：Afly
#   @date          ：2019.06.09
#   @description   ：
#
#================================================================
import sys
import time

S = [10,4,8,7,9,6,2,5,3]
maxprofit = 0
buyday = 0
sellday = 0

#最大获利
for i in range(len(S) - 1):
    for j in range(i+1, len(S)):
        if S[j] - S[i] > maxprofit:
            maxprofit = S[j] - S[i]
            buyday = i
            sellday = j

print("b{0},s{1},maxprofit{2}".format(buyday, sellday,maxprofit))

"""
    判断S中是否有i,j，使得M = S[i] + S[j]
    输入：list,以及 M - S[i]
    返回：
"""
def binaryFind(S, m):
    if len(S) == 0:
        return -1
    i = int(len(S) / 2)
    if S[i] == m:
        return i
    if S[i] > m and i - 1 >= 0:
        return binaryFind(S[0:i-1], m)
    if S[i] < m and i+1 < len(S):
        return binaryFind(S[i: len(S)], m)

    return  -1

start = time.clock()

#将S升序排列
S.sort()
print(S)
M = 9
success = False
for i in range(len(S)):
    m = M - S[i]
    j = binaryFind(S,m)
    if j != -1 and j != i:
        print("存在i和j使得S[{0}] + S[{1}] = {2}".format(i, j, M))
        success = True
        break
if success != True:
    print("不存在i和j使得S[I] + S[J] = {0}".format(M))
elapsed = time.clock() - start
print("Time used:", elapsed)


def twoSum(nums,target):
    d = {}
    for i, num in enumerate(nums):
        if target-num in d:
            return [d[target-num], i]
        print("num:{0},i :{1}".format(num, i))
        d[num] = i
        print("len of dict {0}".format(len(d)))

start = time.clock()
retlist = twoSum(S,9)
if retlist != False:
     print("存在i和j使得S[{0}] + S[{1}] = {2}".format(retlist[0], retlist[1], M))
elapsed = time.clock() - start
print("Time used:", elapsed)