
import sys

# stupid hacked up version
def print_sin_string(str):

    s = ["" for _ in range(3)]
    for i in range(3):
        s[i] = [" " for _ in range(len(str))]

    for i, s1, s2, s3 in zip(
            range(0, len(str), 1),
            range(2, sys.maxsize, 4),
            range(1, sys.maxsize, 2),
            range(0, sys.maxsize, 4)):

        if s1 < len(str):
            s[0][s1] = str[s1]

        if s2 < len(str):
            s[1][s2] = str[s2]

        if s3 < len(str):
            s[2][s3] = str[s3]

    for i in s:
        print("".join(i))

print_sin_string("hello how are you ")
print_sin_string("Google~Worked!")


import sys
import random
import string


# @include
def snake_string(s):
    result = []
    # Outputs the first row, i.e., s[1], s[5], s[9], ...
    for i in range(1, len(s), 4):
        result.append(s[i])
    # Outputs the second row, i.e., s[0], s[2], s[4], ...
    for i in range(0, len(s), 2):
        result.append(s[i])
    # Outputs the third row, i.e., s[3], s[7], s[11], ...
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)


# Python solution uses slicing with right steps.
def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]
# @exclude


def rand_string(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def small_test():
    assert snake_string(
        'Hello World!') == 'e lHloWrdlo!' == snake_string_pythonic(
            'Hello World!') == 'e lHloWrdlo!'


def main():
    small_test()
    s = sys.argv[1] if len(sys.argv) == 2 else rand_string(
        random.randint(1, 100))
    print(snake_string(s))
    assert snake_string(s) == snake_string_pythonic(s)


if __name__ == '__main__':
    main()
