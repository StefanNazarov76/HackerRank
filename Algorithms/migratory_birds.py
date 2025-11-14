#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    counts = Counter(arr)

    best_id = None
    best_freq = -1

    for bird_id, freq in counts.items():
        if freq > best_freq or (freq == best_freq and bird_id < best_id):
            best_freq = freq
            best_id = bird_id

    return best_id


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
