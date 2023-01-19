#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# 

def t_to_string(t):
    s = ""
    i = 0
    while (i < len(t)-1):
        s += t[i] + ':'
        i += 1
    s += t[i]
    return s

def am(s):
    if s[len(s)-2:len(s)] == "AM":
        return True
    else:
        return False
    
def addTwelve(hour):
    h = int(hour)
    h += 12
    return str(h)
    
def amIn24HourFormat(t):
    if t[0] == "12":
        t[0] = "00"
    return t_to_string(t)
    
def pmIn24HourFormat(t):
    if t[0] == "12":
        return t_to_string(t)
    else:
        t[0] = addTwelve(t[0])
        return t_to_string(t)
        
    
def timeConversion(s):
    lastTwoChars = s[len(s)-2:len(s)]
    timeTuple = s[0:len(s)-2].split(':')
    
    if (am(lastTwoChars)):
        return amIn24HourFormat(timeTuple)
    else:
        return pmIn24HourFormat(timeTuple)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()