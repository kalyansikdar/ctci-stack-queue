"""
In case only a minVal variable is maintained as part of the stack class, once the
lowest value is popped, the minVal will not be min anymore. Hence, We have to maintain the min value at every step.
"""
class stk:
    def __init__(self):
        self.arr = []
        self.minVal = None

    def push(self, val):
        if len(self.arr) == 0:
            self.minVal = val
        else:
            if val < self.minVal:
                self.minVal = val
        self.arr.append((val, self.minVal))

    def showMin(self):
        if len(self.arr) > 0:
            return self.arr[-1][1]
        else:
            return None

    def isEmpty(self):
        if len(self.arr)> 0:
            return False
        return True
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            val = self.arr.pop()
            return val

    def show_stack(self):
        print (self.arr)

stack1 = stk()
stack1.push(5)
stack1.push(6)
stack1.push(3)
stack1.push(7)
stack1.show_stack()
print(stack1.showMin())
stack1.pop()
stack1.pop()
stack1.show_stack()
print(stack1.showMin())
stack1.pop()
stack1.pop()
print(stack1.isEmpty())
stack1.showMin()
