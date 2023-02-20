#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    a=max(arr)
    b=min(arr)
    c,d=arr.index(a),arr.index(b)
    m=arr.pop(c)
    min1=sum(arr)
    arr.insert(c,m)
    arr.pop(d)
    max1=sum(arr)
    print(min1,max1)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
    
    This code is contributed by PR.KRITHIKA PRIYA
