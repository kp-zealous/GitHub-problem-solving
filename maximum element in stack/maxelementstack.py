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
    
  
    This code is contributed by PR.KRITHIKA PRIYA
