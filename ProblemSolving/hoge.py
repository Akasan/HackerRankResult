#!/bin/python3

import math
import os
import random
import re
import sys

def make_divisors(n, _min, _max):
    return [i for i in range(_min, n+1) if n % i == 0 and _min <= i <= _max]

def getTotalX(a, b):
    div = []
    append = div.append
    for _b in b:
        _div = make_divisors(_b, a[0], b[0])
        for d in _div:
            if d not in div:
                is_a = all([d % _a == 0 for _a in a])
                is_b = all([_b % d == 0 for _b in b])
                if is_a and is_b:
                    append(d)

    print(div)
    return len(div)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()
