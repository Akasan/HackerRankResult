#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    cnt = Counter(a)
    length = 0

    for base in sorted(cnt.keys(), key=lambda x: x):
        cand = [cnt[base]]
        for comp in sorted(cnt.keys(), key=lambda x: x):
            if abs(base - comp) > 1 or comp <= base:
                continue
            
            cand.append(cand[0] + cnt[comp])
        
        length = max(cand) if max(cand) > length else length

    return length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
