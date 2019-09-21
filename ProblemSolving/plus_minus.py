#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    ratio = [0, 0, 0]
    for item in arr:
        if item > 0:
            ratio[0] += 1
        elif item < 0:
            ratio[1] += 1
        else:
            ratio[2] += 1
    
    ratio = list(map(lambda x: x / length, ratio))
    for item in ratio:
        print(item)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

