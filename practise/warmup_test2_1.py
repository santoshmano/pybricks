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

        return self.data.pop()

def rtoi(strRoman):

    dec = []
    for c in strRoman:
        if c == "I":
            dec.append(1)
        elif c == "V":
            dec.append(5)
        elif c == "X":
            dec.append(10)
        elif c == "L":
            dec.append(50)
        elif c == "X":
            dec.append(10)
        elif c == "L":
            dec.append(50)
        elif c == "C":
            dec.append(100)
        elif c == "D":
            dec.append(500)
        elif c == "M":
            dec.append(1000)

    print(strRoman, dec)

    s = Stack()

    dec_nums = [1, 5, 10, 50, 100, 500, 1000]
    dec_sep = [1, 100, 1000]        # 1, 100, 100 as separate items

    i = len(dec)-1
    while i >= 0:
        print(i, dec[i])
        if i-1 >= 0:
            if (dec[i] > dec[i-1]) and  dec[i] not in dec_sep:
                s.push(dec[i]-dec[i-1])
                i -= 2
                continue
            elif (dec[i] > dec[i-1]) and dec[i] in dec_sep:
                s.push(dec[i])
                s.push(dec[i-1])
                i -= 2
                continue
            elif (dec[i] <= dec[i-1]):
                s.push(dec[i])
                i -= 1
        else:
            s.push(dec[i])
            i -= 1

    sum = 0
    while (not s.isEmpty()):
        num = s.pop()
        print(num)
        sum += num

    return sum

#print(rtoi("IV"))
#print(rtoi("VI"))
#print(rtoi("MIM"))
#print(rtoi("IM"))
#print(rtoi("XCIX"))
print(rtoi("MMMMCMXCIX"))   #4999
#print(rtoi("IX"))   #9
#print(rtoi("MMXV")) #2015
#print(rtoi("X"))   #9
