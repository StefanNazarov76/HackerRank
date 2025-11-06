#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    specials = set('!@#$%^&*()-+')
    categories = {
        'digit': any(ch.isdigit() for ch in password),
        'lower': any(ch.islower() for ch in password),
        'upper': any(ch.isupper() for ch in password),
        'special': any(ch in specials for ch in password),
    }

    missing_types = sum(not v for v in categories.values())

    return max(missing_types, 6 - n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
