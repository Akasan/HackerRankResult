# I refered this excellent answer
# https://www.hackerrank.com/rest/contests/master/challenges/magic-square-forming/hackers/majkS/download_solution?primary=true
# implemented by https://www.hackerrank.com/profile/majkS

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations


def formingMagicSquare(s):
    s = s[0] + s[1] + s[2]
    cost = 100
    for p in permutations(range(1, 10)):
        is_row = all([sum(p[:3])==15, sum(p[3:6])==15, sum(p[6:])==15])
        is_col = all([sum(p[::3])==15, sum(p[1::3])==15, sum(p[2::3])==15])
        is_cross = all([(p[0]+p[4]+p[8])==15, (p[2]+p[4]+p[6])==15])
        if is_row and is_col and is_cross:
            cost = min(cost, sum([abs(p[i] - s[i]) for i in range(9)]))

    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
