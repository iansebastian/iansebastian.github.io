#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    result = []
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        bin_k = list(bin(k))[2:]

        m = 0
        while (2**m-1 <= n):
            m += 1
        m -= 1
        
        tes = 2**m - 1

        if k<=tes:
            maks = k-1
        else:
            if k%2 == 0:
                bin_n = list(bin(n))[2:]
                bin_k1 = list(bin(k-1))[2:]

                if len(bin_k1) < len(bin_n):
                    bin_k1 = ['0'] + bin_k1
                
                lim = 0
                while bin_n[lim] == bin_k1[lim]:
                    lim += 1

                if '0' in bin_k1[lim+1:]:
                    excp = False
                elif bin_k1[lim+1:] == bin_n[lim+1:]:
                    excp = False
                else:
                    excp = True

                if excp:
                    maks = k-2
                else:
                    maks = k-1
            else:
                maks = k-1
        result.append(maks)

    for stuff in result:
        print(stuff)