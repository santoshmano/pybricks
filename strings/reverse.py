
def reverse(s):
    for i in range(len(s)//2):
        s[i], s[~i] = s[~i], s[i]
    return s

def reverse_range(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end = end -1
    return s

def reverse_words_line(l):
    reverse(l)
    start, end = 0, 0
    while start < len(l)-1:

        while start < len(l)-1 and not l[start].isalnum():
            start += 1
            end += 1

        while end < len(l)-1 and l[end].isalnum():
            end += 1

        end += 1
        reverse_range(l, start, end-1)
        start = end
    return l

if __name__ == "__main__":

    strings = ["", "hello", "h", "si", "ss", "si", "malayalam"]
    for s in strings:
        print("s =", s, "\n", "rev =", "".join(reverse(list(s))))

    for s in strings:
        print("s =", s, "\n", "rev =", "".join(reverse_range(list(s), 1, len(s)-1)))

    lines = ["abc xyz",
             "hello mother earth",
             "",
             "A man, a plan, a canal, Panama",
             "Able was I, ere I saw Elba!",
             "Ray a Ray"]

    for l in lines:
        print("l =", l, "\n", "rev =", "".join(reverse_words_line(list(l))))
