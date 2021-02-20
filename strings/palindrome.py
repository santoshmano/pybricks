def is_palindrome_word(s):
    if len(s) == 0 or len(s) == 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome_word(s[1:-1])
    else:
        return False

def is_palindrome_word_iter(s):

    for i in range(len(s)//2):
        if s[i] != s[~i]:
            return False

    return True

# ignore non-alphanum
def is_palindrome_line(s):

    if len(s) == 0 or len(s) == 1:
        return True

    if s[0].isalnum() != True:
        return is_palindrome_line(s[1:])

    if s[-1].isalnum() != True:
        return is_palindrome_line(s[:-1])

    if s[0].lower() == s[-1].lower():
        return is_palindrome_line(s[1:-1])

    return False


if __name__ == "__main__":

    strings = ["", "hello", "h", "si", "ss", "si", "malayalam"]
    for s in strings:
        print("s =", s, "\n",
              is_palindrome_word(s),
              is_palindrome_word_iter(s))


    lines = ["hello",
             "",
             "   ;(*&((*&",
             "A man, a plan, a canal, Panama",
             "Able was I, ere I saw Elba!",
             "Ray a Ray"]

    for l in lines:
        print("l =", l, "\n",
              is_palindrome_line(l))
