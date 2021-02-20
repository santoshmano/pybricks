#TODO: implement with Exception handling

class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, val):
        return self.data.append(val)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.data.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.data[-1]

if __name__ == "__main__":
    stk = Stack()
    stk.push(10)
    stk.push(12)

    for i in range(1,4):
        print(stk.pop())
