#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    result = []

    for n in range(p, q + 1):
        n_sq = n ** 2
        n_sq_str = str(n_sq)
        d = len(str(n))

        r = n_sq_str[-d:]
        l = n_sq_str[:-d] or '0'

        if int(l) + int(r) == n:
            result.append(n)

    if result:
        print(*result)
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
