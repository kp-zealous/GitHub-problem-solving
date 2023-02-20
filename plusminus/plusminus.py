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
    m=len(arr)
    p,n,z=0,0,0
    for i in arr:
      if i==0:
        z+=1
      elif i>0:
        p+=1
      else:
        n+=1 
    print('%.6f' % (p/m))
    print('%.6f' % (n/m))
    print('%.6f' % (z/m))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

 
This code is contributed by PR.KRITHIKA PRIYA
