#!/bin/python3
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwapsNaive(arr):
    i = 0
    swaps = 0
    while i < len(arr):
        if arr[i] != i+1:
            swaps += 1
            j = i+1
            while arr[j] != i+1:
                j += 1
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return swaps

def minimumSwaps(arr):
    i = 0
    swaps = 0
    # new = [None for i in range(len(arr))]
    # n = 0
    while i < len(arr):
        if arr[i] == i+1:
            # new[i] = arr[i]
            arr[i] = None
            i += 1
            # n += 1
        elif arr[i] is not None:
            # new[arr[i]-1] = arr[i]
            temp = i
            i = arr[i]-1
            arr[temp] = None
            swaps += (arr[i] != None)
            # n+=1
        elif arr[i] is None:
            i += 1
    return swaps
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
