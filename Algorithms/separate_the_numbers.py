#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n = len(s)
    found = False

    for i in range(1, n // 2 + 1):
        if s[0] == '0':
            break

        first = int(s[:i])
        num = first
        temp = str(num)

        while len(temp) < n:
            num += 1
            temp += str(num)

        if temp == s:
            print('YES', first)
            found = True
            break

    if not found:
        print('NO')

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
