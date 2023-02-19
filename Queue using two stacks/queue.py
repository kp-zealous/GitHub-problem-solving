import math
import os
import random
import re
import sys
class queue:
  def __init__(self):
      self.items=[]
  def enqueue(self,x):
    self.items.append(x)
  def dequeue(self):
    if self.items==[]:
      return 0
    self.items.pop(0)
  def printele(self):
    return self.items[0]

def getMax(op):
  q1=queue()
  res=[]
  for i in op:
    i=i.split(" ")
    if eval(i[0])==1:
      q1.enqueue(eval(i[1]))
    elif eval(i[0])==2:
      q1.dequeue()
    elif eval(i[0])==3:
      res.append(q1.printele())
  return res
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
