#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair_idx = []

    for i, a in enumerate(ar):
        if i in pair_idx:
            continue
        
        try:
            idx = ar[i+1:].index(a) + i + 1
            pair_idx.append(i)
            pair_idx.append(idx)
        except:
            continue

    return len(pair_idx) // 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
