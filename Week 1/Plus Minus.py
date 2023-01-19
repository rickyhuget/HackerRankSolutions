#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    size = len(arr)
    pos = 0.0
    neg = 0.0
    zero = 0.0
    for x in arr:
        if x > 0: pos += 1
        elif x < 0: neg += 1
        else: zero += 1
    pos = pos/size
    neg = neg/size
    zero = zero/size
    print("{0:.6f}".format(pos))
    print("{0:.6f}".format(neg))
    print("{0:.6f}".format(zero))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)