#!/usr/bin/python3

"""isWinner Module"""


def isWinner(x, nums):
    """Prime numbers game"""
    if x < 0 or nums[-1] < 1:
        return None
    Maria_score = 0
    Ben_score = 0
    max_num = max(nums) + 1
    prime_number = [False] * max_num 
    p = []
    for i in range(2, max_num):
        if not prime_number[i]:
            p.append(i)
            for j in range(i, max_num , i):
                prime_number[j] = True

    l = 0
    for a0 in range(x):
        n = nums[l]
        num = 0
        for x in range(max_num):
            if x >= len(p) or p[x] > n:
                break
            num += 1
        l += 1
        if num % 2 == 1:
            Maria_score += 1
        else:
            Ben_score += 1
    if Maria_score > Ben_score:
        return "Maria"
    else if Ben_score < Maria_score:
        return "Ben"
    else
        return None
