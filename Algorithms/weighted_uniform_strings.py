#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here

    weights = set()
    prev_char = ''
    curr_weight = 0

    for c in s:
        val = ord(c) - ord('a') + 1
        if c == prev_char:
            curr_weight += val
        else:
            curr_weight = val
            prev_char = c
        weights.add(curr_weight)

    return ['Yes' if q in weights else 'No' for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
