#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours, mins, secs = s.split(':')

    if 'AM' in s and '12' in hours:
        hours = '00'
    elif 'PM' in s and '12' not in hours:
        hours = int(hours) + 12

    secs = secs[:2]

    return f'{hours}:{mins}:{secs}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
