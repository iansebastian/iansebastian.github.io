#!/bin/python3
# https://www.hackerrank.com/challenges/crush
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]
    maks = 0
    jlh = 0
    for i in range(len(queries)):
        if queries[i][0] > 0:
            arr[queries[i][0]-1] += queries[i][2]
        if queries[i][1] < len(arr):
            arr[queries[i][1]] -= queries[i][2]
    for ele in arr:
        jlh += ele
        if jlh > maks:
            maks = jlh
    return maks


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
