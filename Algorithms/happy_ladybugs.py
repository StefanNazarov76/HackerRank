#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    if '_' not in b:
        for i in range(len(b)):
            left_same = (i > 0 and b[i] == b[i - 1])
            right_same = (i < len(b) - 1 and b[i] == b[i + 1])
            if not (left_same or right_same):
                return 'NO'
        return 'YES'

    counts = Counter(b)

    for color, cnt in counts.items():
        if color != '_' and cnt == 1:
            return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
