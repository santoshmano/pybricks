def all_strings_ascending(str):
    for start in range(0, len(str)):
        for end in range(start+1, len(str)+1):
            print(str[start:end])

def is_palindrome(str):
    start = 0
    end = len(str)-1

    while start < len(str)//2:
        if str[start] != str[end]:
            return False
        end -= 1
        start += 1

    return True    

def is_palindrome_rec(str):
    if len(str) == 0 or len(str) == 1:
        return True

    if str[0] != str[-1]:
        return False
    else:
        return is_palindrom_rec(str[1:-1])

# len from len to 1
# start from 0 to len//2
# end from  
def all_strings_descending(str):
    for length in range(len(str), 0, -1):
        for start in range(0, len(str)-1):
            end = start+length
            if end > len(str):
                break
            if is_palindrome(str[start:end]):
                print("string", str)
                print("biggest palindrome:", str[start:end])
                return


print("ascending")
all_strings_ascending("abaa")
print("descending")
all_strings_descending("abaa")
