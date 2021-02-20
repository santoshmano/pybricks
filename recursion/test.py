s = ['2', ' ', '3', '+', 'a', 'a;lsdfj', '222']

for i in s:
    print(i)
    if i.isalpha():
        print("isalpha")
    elif i.isnumeric():
        print("isnumeric")
    elif i.isspace():
        print("isspace")
    elif i == '+':
        print("isoperator")
