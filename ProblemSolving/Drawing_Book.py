#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if p == 1 or p == n:
        return 0

    for i in range(n//2):
        front = [2 * i, 2 * i + 1]
        back = [n - 2 * i]
        if i == 0 and n % 2 == 1:
            back.append(n - 1)
        elif i > 0 and n % 2 == 0:
            back.append(n - 2 * i + 1)
        elif i > 0 and n % 2 == 1:
            back.append(n - 2 * i - 1)
        
        print(front, back)
        if p in front or p in back:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()
