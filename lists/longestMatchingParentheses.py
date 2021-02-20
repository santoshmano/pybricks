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

def longestSubstring(expr):

    stk = ArrayStack()
    subLen = 0
    prevLen = 0

    for c in expr:
        if c == '(':
            stk.push(c)
            if subLen:
                prevLen = subLen
                subLen = 0
            print(subLen, prevLen)
        elif c == ')':
            if stk.isEmpty():
                if prevLen < subLen:
                    prevLen = subLen
                subLen = 0
                print(subLen, prevLen)
            else:
                stk.pop()
                subLen += 2
                print(subLen)

    print("end", subLen, prevLen)
    if stk.isEmpty():
        return subLen+prevLen
    elif subLen > prevLen:
        return subLen
    else:
        return prevLen

print("length of - ()(())", longestSubstring("()(())"))
#print("length of - ((((", longestSubstring("(((("))
#print("length of - ()()()", longestSubstring("()()()"))
#print("length of -", longestSubstring(""))



