#!/bin/python3

import math
import os
import random
import re
import sys
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
def equalStacks(h1, h2, h3):
  a,b,c,i,h=sum(h1),sum(h2),sum(h3),0,0
  while i>=0:
    if a==b and b==c:
       h=a
       break
    d=maximum(a,b,c)
    if a==d:
      a-=h1[0]
      h1.pop(0)
    elif b==d:
      b-=h2[0]
      h2.pop(0)
    elif c==d:
      c-=h3[0]
      h3.pop(0)
    i=i+1
  return h
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
