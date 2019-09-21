#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hms = s.split(":")
    is_pm = "PM" in hms[-1]
    if is_pm:
        if not int(hms[0]) >= 12:
            hour = (int(hms[0]) + 12)
        else:
            hour = int(hms[0])
    else:
        hour = int(hms[0]) % 12

    hour = str(hour).zfill(2)
    return ":".join([hour, hms[1], hms[2][:2]])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

