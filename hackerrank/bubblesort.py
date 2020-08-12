#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(len(a)-1):
        for j in range (i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
    print("Array is sorted in", count, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
