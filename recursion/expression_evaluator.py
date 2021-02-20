'''
todo
- Redo the below code to not modify input string.
- Add error conditions.
- make functions more generic to accept any operators/expressions
'''

def getElements(s, n, stack):
    if n >= len(s):
        return

    print(s, n, stack)
    if s[n].isnumeric():
        num = 0
        while s[n].isnumeric():
            num = num*10 + int(s[n])
            n += 1
            if n >= len(s):
                break
        stack.append(num)
    elif s[n] == '+':
        stack.append(s[n])
        n += 1
    elif s[n] == '*':
        num1 = stack.pop()
        n += 1
        num2 = 0
        while s[n].isnumeric():
            num2 = num2 * 10 + int(s[n])
            n += 1
            if n >= len(s):
                break
        num1 *= num2
        stack.append(num1)

    getElements(s, n, stack)

# this code works only on '+', if there is a '-' the logic has to change
# todo add error checks
def evalElements(stack):
    result = 0

    if (stack != []):
        result = stack.pop()
    else:
        return result

    if result:
        while stack != []:
            operator = stack.pop()
            print(stack)
            num2 = stack.pop()
            print(stack)

            if operator == '+':
                result += num2
            else:
                print("Error, unexpected stack element")
                return 0

            print(result)

    return result

def getExpression(s, n):
    if n >= len(s)-1:
        if (expressionEval(s) == 24):
            print(s, "print s", "n=", n)
        return

    for operator in ('', '*', '+'):
        if s[n] == '?':
            s[n] = operator

        getExpression(s, n+2)

        if s[n] == '' or s[n] == '*' or s[n] == '+':
            s[n] = '?'
    return

def getExpressionMain(s):
    # insert ? inbetween every pair of numbers
    for i in range(1, 2*len(s)-1, 2):
        s.insert(i, '?')
    getExpression(s, 1)

getExpressionMain(list("333"))