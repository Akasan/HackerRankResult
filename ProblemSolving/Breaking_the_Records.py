#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    _min = scores[0]
    _max = scores[0]
    min_cnt = 0
    max_cnt = 0

    for score in scores[1:]:
        if _min > score:
            _min = score
            min_cnt += 1
        elif _max < score:
            _max = score
            max_cnt += 1
    
    return [max_cnt, min_cnt]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
