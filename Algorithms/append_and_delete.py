#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    common = 0
    for cs, ct in zip(s, t):
        if cs == ct:
            common += 1
        else:
            break

    ops_needed = (len(s) - common) + (len(t) - common)

    if k >= len(s) + len(t):
        return 'Yes'

    if k >= ops_needed and (k - ops_needed) % 2 == 0:
        return 'Yes'

    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
