#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]

    if len(left) != len(right):
        return -1

    c_left = Counter(left)
    c_right = Counter(right)
    diff = c_left - c_right

    return sum(diff.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
