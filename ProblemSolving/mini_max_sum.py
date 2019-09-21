#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[:-1])
    max_sum = sum(sorted_arr[1:])
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

