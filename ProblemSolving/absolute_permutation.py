#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    solution = {}
    ran = range(1, n + 1)
    min_diff = [abs(i - k) for i in ran]
    max_diff = [abs(i + k) for i in ran]

    for i, (_min, _max) in enumerate(zip(min_diff, max_diff), 1):
        if i > k and not _min in solution.keys():
            solution[_min] = None
        else:
            if _max > n:
                return [-1]

            solution[_max] = None

    return list(solution.keys())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

