import math
import os
import random
import re
import sys
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
        
    def prints(self):
        return max(self.items)
def getMax(operations):
    stack = Stack()
    m=[]
    for i in operations:
        i=i.split(" ")
        if eval(i[0])==1:
            stack.push(int(i[1]))
        elif eval(i[0])==2:
            stack.pop()
        else:
            m.append(stack.prints())
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

    
    
  
    This code is contributed by PR.KRITHIKA PRIYA
