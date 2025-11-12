#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    unique_chars = list(set(s))
    max_len = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1, c2 = unique_chars[i], unique_chars[j]

            filtered = [ch for ch in s if ch == c1 or ch == c2]

            if all(filtered[k] != filtered[k + 1] for k in range(len(filtered) - 1)):
                max_len = max(max_len, len(filtered))

    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
