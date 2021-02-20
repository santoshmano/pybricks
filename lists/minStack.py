from stack import *

class MinStack:
    def __init__(self):
        self.dataStk = ArrayStack()
        self.minStk = ArrayStack()

    def pop(self):
        data = self.dataStk.pop()
        if data == self.minStk.peek():
            self.minStk.pop()

        return data

    def push(self, val):
        if not self.minStk.isEmpty():
            if val < self.minStk.peek() or val == self.minStk.peek():
                self.minStk.push(val)
        else:
            self.minStk.push(val)

        self.dataStk.push(val)

    def getMin(self):
        return self.minStk.peek()

    def peek(self):
        return self.dataStk.peek()

if __name__ == "__main__":

    mStk = MinStack()

    mStk.push(14)
    mStk.push(16)
    mStk.push(14)
    mStk.push(43)
    mStk.push(15)
    mStk.push(13)
    mStk.push(13)
    mStk.push(12)

    print("top of mstk ", mStk.peek())
    print("min - ", mStk.getMin())
    print("pop - ", mStk.pop())

    print("min - ", mStk.getMin())
    print("pop - ", mStk.pop())

    print("min - ", mStk.getMin())
    print("pop - ", mStk.pop())

    print("min - ", mStk.getMin())
"""
    """
