#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n=len(arr)
    s1,s2=0,0
    j,k=n,n
    for i in range(n):
      for j in range(n):
        if i==j:
          s1+=arr[i][j]
    for i in range(0,len(arr)):
         k=k-1
         s2+=arr[i][k]
    return(abs(s2-s1))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    This code is contributed by PR.KRITHIKA PRIYA
