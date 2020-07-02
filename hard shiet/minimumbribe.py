#!/bin/python3
#https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=arrays
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            return "Too chaotic"
        elif q[i] - (i+1) <= 0:
            if i >= 1:
                for j in range (max(q[i]-2, 0), i):
    return bribes


if __name__ == '__main__':
    res = []
    t = int(input())
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        res.append(minimumBribes(q))
    for ele in res:
        print(ele)