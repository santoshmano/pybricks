
class ArrayStack:

    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, val):
        return self.data.append(val)

    def pop(self):
        if self.isEmpty():
            raise Empty("Stack underflow!")

        return self.data.pop()

    def peek(self):
        if self.isEmpty():
            raise Empty("Stack is empty!")

        return self.data[-1]


def hasMatchingParantheses(expr):
    stk = ArrayStack()

    left = '({['
    right = ')}]'

    for c in expr:
        print(c, stk.data)
        if c in left:
            stk.push(c)
        elif c in right:
            if stk.isEmpty():
                return False
            else:
                if left.index(stk.pop()) != right.index(c):
                    return False
        else:
            continue

    return stk.isEmpty()


print(hasMatchingParantheses("((3+4))"))
