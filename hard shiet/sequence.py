import math
import os
import random
import re
import sys

(N, M, K) = tuple(map(int, input().rstrip().split()))

A = []
B = []
C = []

for i in range(N):
    (A_i, B_i, C_i) = tuple(map(int, input().rstrip().split()))
    A.append(A_i)    
    B.append(B_i)
    C.append(C_i)

for i in range(N):
    for j in range(C[i]):
        
