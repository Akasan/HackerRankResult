#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy

# Complete the bomberMan function below.
def bomberMan(n, grid):
    result = deepcopy(grid)
    result = list(map(lambda x:x.replace(".", "O"), result))
    result = list(map(lambda x: list(x), result))
    grid_cp = deepcopy(grid)
    grid_cp = list(map(lambda x:list(x), grid_cp))

    bomb_pos = []

    for row, line in enumerate(grid_cp):
        for col, p in enumerate(list(line)):
            if p == "O":
                bomb_pos.append((row, col))
    
    for row, col in bomb_pos:
        result[row][col] = "."
        if row >= 1:
            result[row-1][col] = "."
        if row < len(grid_cp) -1:
            result[row+1][col] = "."
        
        if col >= 1:
            result[row][col-1] = "."
        if col < len(grid_cp[0]) -1:
            result[row][col+1] = "."
    
    result = list(map(lambda x:"".join(x), result))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

