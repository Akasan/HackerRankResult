#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def update_height(pre_height, s):
    return pre_height -1 if s == "D" else pre_height + 1
    
def countingValleys(n, s):
    cnt = 0
    height = -1 if s[0] == "D" else 1  
    pre_height = height
    
    for _s in s[1:]:
        height = update_height(height, _s)
        if height == 0 and pre_height < 0:
            cnt += 1
        
        pre_height = height
    
    return cnt

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
