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

def timeConversion(s):
    hour=int(s[:2])%12
    if s[8]=='P':
      hour+=12
    if s[-2:]=='AM':
      return ('0'+str(hour)+s[2:8])
    else:
      return (str(hour)+s[2:8])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

    
    This code is contributed by PR.KRITHIKA PRIYA
