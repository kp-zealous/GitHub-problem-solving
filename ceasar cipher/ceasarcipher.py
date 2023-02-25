#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    res=''
    for i in s:
        if i.isupper():
            res+=chr((ord(i)+k-65)%26+65)
        elif i.islower():
            res+=chr((ord(i)+k-97)%26+97)
        else:
            res+=i
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

    
    
    
    This code is contributed by PR.KRITHIKA PRIYA
