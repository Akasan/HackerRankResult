#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year < 1918:
        is_leap = True if year % 4 == 0 else False
    elif year > 1918:
        is_400 = True if year % 400 == 0 else False
        is_other = True if year % 4 == 0 and year % 100 != 0 else False
        is_leap = True if is_400 or is_other else False
    else:
        return "26.09.1918"

    return f"12.09.{year}" if is_leap else f"13.09.{year}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()
