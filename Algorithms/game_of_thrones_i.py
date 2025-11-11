#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here

    counter = Counter(s)
    odd_freq = sum(1 for freq in counter.values() if freq % 2 == 1)
    return 'NO' if odd_freq > 1 else 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
