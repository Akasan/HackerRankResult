#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    tmp1 = [a[0] > b[0], a[1] > b[1], a[2] > b[2]]
    tmp2 = [a[0] == b[0], a[1] == b[1], a[2] == b[2]]
    a_cnt = tmp1.count(True)
    b_cnt = 3 - a_cnt
    
    for i, item in enumerate(tmp2):
        if item == True:
            a_cnt -= 1 if tmp1[i] == True else 0
            b_cnt -= 1 if tmp1[i] == False else 0

    return [a_cnt, b_cnt]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

