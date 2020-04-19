#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    cnt = 1
    if x1 != x2 and v1 == v2:
        return "NO"
    
    while True:
        _x1 = x1 + v1 * cnt
        _x2 = x2 + v2 * cnt
        if _x1 == _x2:
            return "YES"
            
        if (v1 > v2 and _x1 > _x2) or (v1 < v2 and _x1 < _x2):
            return "NO"
            
        cnt += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()
