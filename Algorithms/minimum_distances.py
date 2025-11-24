#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    last_seen = {}
    min_dist = len(a) + 1

    for i, val in enumerate(a):
        if val in last_seen:
            dist = i - last_seen[val]
            if dist < min_dist:
                min_dist = dist
        last_seen[val] = i

    return min_dist if min_dist <= len(a) else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
