"""
Solutions to CodingBat Recursion-1 problems in python
http://codingbat.com/java/Recursion-1

copyright of problems belong to codingbat.com
copyright of the testdriver belongs to cbmurphy
solutions to the problems are mine, you are free to copy it
"""

"""
Problem:
Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1.
Compute the result recursively (without loops).

factorial(1) → 1
factorial(2) → 2
factorial(3) → 6
"""
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

"""
Problem:
We have a number of bunnies and each bunny has two big floppy ears. We want
to compute the total number of ears across all the bunnies recursively (without
loops or multiplication).

bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4
"""
def bunnyEars(bunnies):

    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)

"""
Problem:
The fibonacci sequence is a famous bit of mathematics, and it happens to
have a recursive definition. The first two values in the sequence are 0
and 1 (essentially 2 base cases). Each subsequent value is the sum of
the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8,
13, 21 and so on. Define a recursive fibonacci(n) method that returns
the nth fibonacci number, with n=0 representing the start of the sequence.

fibonacci(0) → 0
fibonacci(1) → 1
fibonacci(2) → 1

Solution:
       { 0, n == 0
f(n) = { 1, n == 1
       { f(n-1) + f(n-2), n

time O(N) = 2**N
"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

"""
Problem:
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
(1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll
say have 3 ears, because they each have a raised foot. Recursively
return the number of "ears" in the bunny line 1, 2, ... n (without
loops or multiplication).

bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5

Solution:

nth bunny
       { 0, n==0
b(n) = { 2, n==odd and n>0
       { 3, n==even and n>0

total bunnies in line
tb(n) = { b(n) + tb(n-1)

"""
def bunnyEars2(bunnies):
    if bunnies == 0:
        return 0

    if bunnies % 2 == 0:
        nth_bunny_ears = 3
    else:
        nth_bunny_ears = 2

    return nth_bunny_ears + bunnyEars2(bunnies-1)

"""
Problem:
We have triangle made of blocks. The topmost row has 1 block,
the next row down has 2 blocks, the next row has 3 blocks, and
so on. Compute recursively (no loops or multiplication) the total
number of blocks in such a triangle with the given number of rows.

triangle(0) → 0
triangle(1) → 1
triangle(2) → 3

Solution:
t(rows) = { rows + t(rows-1)
"""

def triangle(rows):
    if rows == 0:
        return 0

    return rows + triangle(rows-1)

"""
Problem:
Given a non-negative int n, return the sum of its digits recursively
(no loops). Note that mod (%) by 10 yields the rightmost digit
(126 % 10 is 6), while divide (/) by 10 removes the rightmost digit
(126 / 10 is 12).

sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3

"""
def sumDigits(n):
    if n == 0:
        return 0

    return sumDigits(n//10) + n%10


"""
Problem:
Given a non-negative int n, return the count of the occurrences of
7 as a digit, so for example 717 yields 2. (no loops). Note that mod
(%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/)
by 10 removes the rightmost digit (126 / 10 is 12).

count7(717) → 2
count7(7) → 1
count7(123) → 0

Solution:

"""
def count7(num):
    if num == 0:
        return 0
    return (1 if(num % 10 == 7) else 0) + count7(num//10)

"""
Problem:
Given a non-negative int n, compute recursively (no loops) the count
of the occurrences of 8 as a digit, except that an 8 with another 8
immediately to its left counts double, so 8818 yields 4. Note that mod (%)
by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10
removes the rightmost digit (126 / 10 is 12).

count8(8) → 1
count8(818) → 2
count8(8818) → 4
"""

def count8(num):
    if num == 0:
        return 0

    if num%10 == 8:
        if (num//10)%10 == 8:
            count = 2
        else:
            count = 1
    else:
        count = 0

    return count8(num//10) + count


"""
Problem:
Given base and n that are both 1 or more, compute recursively (no loops)
the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27

Solution:

p(base, n) = { 1, n==0
             { base * p(base, n-1) , n>0

"""
def powerN(base, num):

    if num == 0:
        return 1

    return base * powerN(base, num-1)


"""
Problem:
Given a string, compute recursively (no loops) the number of lowercase 'x'
chars in the string.

countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
"""

def countX(str):
    if len(str) == 0:
        return 0

    return (1 if str[0] == "x" else 0) + countX(str[1:])


"""
Problem:
Given a string, compute recursively (no loops) the number of times lowercase
"hi" appears in the string.

countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
"""

def countHi(str):
    if len(str) < 2:
        return 0
    if str[:2] == "hi":
        count = 1
    else:
        count = 0
    return count + (countHi(str[2:]) if count else countHi(str[1:]))

"""
Problem:
Given a string, compute recursively (no loops) a new string where all the
lowercase 'x' chars have been changed to 'y' chars.

changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"

Solution:

cxy(str) =
"""

def changeXY(str):

    if str == "":
        return ""

    if str[0] == "x":
        return "y" + changeXY(str[1:])
    else:
        return str[0] + changeXY(str[1:])


"""
Problem:
Given a string, compute recursively (no loops) a new string where all
appearances of "pi" have been replaced by "3.14".

changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"

"""

def changePi(pistr):

    if len(pistr) < 2:
        return pistr

    if pistr[0:2] == "pi":
        return "3.14" + changePi(pistr[2:])

    return pistr[0] + changePi(pistr[1:])

"""
Problem:
Given a string, compute recursively a new string where all the 'x' chars
have been removed.

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""

"""

def noX(str):

    if len(str) == 0:
        return str

    if str[0] == "x":
        return noX(str[1:])

    return str[0] + noX(str[1:])

"""
Problem:
Given an array of ints, compute recursively if the array contains a 6. We'll
use the convention of considering only the part of the array that begins at
the given index. In this way, a recursive call can pass index+1 to move down
the array. The initial call will pass in index as 0.

array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
"""

def array6(arr, index):

    if index >= len(arr):
        return False

    if arr[index] == 6:
        return True

    return array6(arr, index+1)


"""
Problem:

Given an array of ints, compute recursively the number of times that the value
11 appears in the array. We'll use the convention of considering only the part
of the array that begins at the given index. In this way, a recursive call can
pass index+1 to move down the array. The initial call will pass in index as 0.

array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0

"""

def array11(arr, index):
    """
    :return: number of times 11 occurs in arr
    """
    if index >= len(arr):
        return 0

    if arr[index] == 11:
        return 1 + array11(arr, index+1)
    else:
        return array11(arr, index+1)
"""
Problem:
Given an array of ints, compute recursively if the array contains somewhere a
value followed in the array by that value times 10. We'll use the convention of
considering only the part of the array that begins at the given index. In this
way, a recursive call can pass index+1 to move down the array. The initial call
will pass in index as 0.

array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
"""

def array220(arr, index):

    if index >= len(arr)-1:
        return False

    for i in range(index+1, len(arr)):
        if arr[i] / 10 == arr[index]:
            return True

    return array220(arr, index+1)


"""
Problem:

Given a string, compute recursively a new string where all the adjacent chars are
now separated by a "*".

allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"

"""

def allStar(str):

    if len(str) < 2:
        return str

    return str[0] + "*" + allStar(str[1:])

"""
Problem:
Given a string, compute recursively a new string where identical chars that are
adjacent in the original string are separated from each other by a "*".

pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
"""

def pairStar(str):

    if len(str) < 2:
        return str

    if str[0] == str[1]:
        return str[0] + "*" + pairStar(str[1:])

    return str[0] + pairStar(str[1:])

"""
Problem:
Given a string, compute recursively a new string where all the lowercase 'x' chars
have been moved to the end of the string.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
"""

def endX(str):

    if len(str) == 0:
        return str

    if str[0] == "x":
        return endX(str[1:]) + "x"

    return str[0] + endX(str[1:])

"""
Problem:

We'll say that a "pair" in a string is two instances of a char separated by a char.
So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2
for A and 1 for x. Recursively compute the number of pairs in the given string.

countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
"""
def countPairs(str):
    if len(str) < 3:
        return 0

    if str[0] == str[2]:
        return 1 + countPairs(str[1:])

    return countPairs(str[1:])

"""
Problem:
Count recursively the total number of "abc" and "aba" substrings that appear in
the given string.

countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
""
def countAbc(str):

    if len(str) < 3:
        return 0

    if str[:3] == "abc" or str[:3] == "aba":
        return 1 + countAbc(str[1:])

    return countAbc(str[1:])
"""
Problem:
Given a string, compute recursively (no loops) the number of "11" substrings in
the string. The "11" substrings should not overlap.

count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
"""

def count11(str):
    if len(str) < 2:
        return 0

    if str[:2] == "11":
        return 1 + count11(str[2:])

    return count11(str[1:])



"""
Problem:
Given a string, return recursively a "cleaned" string where adjacent chars that
are the same have been reduced to a single char. So "yyzzza" yields "yza".

stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
"""

def stringClean(str):

    if len(str) < 2:
        return str

    index = 1
    while index < len(str) and str[index] == str[0]:
        index += 1

    return str[0] + stringClean(str[index:])



"""
Problem:
Given a string, compute recursively the number of times lowercase "hi" appears
in the string, however do not count "hi" that have an 'x' immediately before them.

countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
"""

def countHi2(str):

    if len(str) < 2:
        return 0

    if str[:2] == "hi":
        return 1 + countHi2(str[2:])

    if len(str) > 2 and str[:3] == "xhi":
        return countHi2(str[3:])

    if len(str) > 2 and str[1:3] == "hi":
        return 1 + countHi2(str[3:])

    return countHi2(str[1:])



"""
Problem:
Given a string that contains a single pair of parenthesis, compute recursively
a new string made of only of the parenthesis and their contents, so
"xyz(abc)123" yields "(abc)".

parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
"""

def parenBit(str):
    if len(str) < 2:
        return ""

    if str[0] == "(" and str[-1] == ")":
        return str

    if str[0] != "(":
        return parenBit(str[1:])

    if str[-1] != ")":
        return parenBit(str[:-1])


"""
Problem:
Given a string, return true if it is a nesting of zero or more pairs of
parenthesis, like "(())" or "((()))". Suggestion: check the first and
last chars, and then recur on what's inside them.

nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
"""



"""
Problem:
Given a string and a non-empty substring sub, compute recursively the number
of times that sub appears in the string, without the sub strings overlapping.

strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0
"""


"""
Problem:

Given a string and a non-empty substring sub, compute recursively if at
least n copies of sub appear in the string somewhere, possibly with
overlapping. N will be non-negative.

strCopies("catcowcat", "cat", 2) → true
strCopies("catcowcat", "cow", 2) → false
strCopies("catcowcat", "cow", 1) → true
"""


"""
Problem:

Given a string and a non-empty substring sub, compute recursively the largest
substring which starts and ends with sub and return its length.

strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
"""


# https://github.com/cbmurphy/Class_Code/blob/master/Intro%20Programming/recursion1.py
# Note from Author - Do not edit anything below this line
def main(argv):

    problems = ["factorial", "bunnyEars", "fibonacci", "bunnyEars2", "triangle", "sumDigits", "count7", "count8",
                "powerN", "countX", "countHi", "changeXY", "changePi", "noX", "array6", "array11", "array220",
                "allStar", "pairStar", "endX", "countPairs", "countAbc", "count11", "stringClean", "countHi2",
                "parenBit", "nestParen", "strCount", "strCopies", "strDist"]

    if len(argv) == 0:
        printHelp()
        exit(1)
    elif "all" in argv:
        argv = problems

    for problem in argv:
        if not problem in problems:
            printHelp()
            exit(1)

    factorial_args = [1, 2, 3, 4, 5, 6]
    bunnyEars_args = [0, 1, 2, 3, 5, 4, 12]
    fibonacci_args = [0, 1, 2, 3, 4, 5, 6, 7]
    bunnyEars2_args = [0, 1, 2, 3, 4, 5, 6, 10]
    triangle_args = [0, 1, 2, 3, 4, 5, 6, 7]
    sumDigits_args = [126, 49, 12, 10, 1, 0, 730, 1111, 11111, 10110, 235]
    count7_args = [717, 7, 123, 77, 7123, 771237, 771737, 47571, 777777, 70701277, 777576197, 99999, 99799]
    count8_args = [8, 818, 8818, 8088, 123, 81238, 88788, 8234, 2348, 23884, 0, 1818188, 8818181, 1080, 188, 88888,
                   9898, 78]
    powerN_args = [(3, 1), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (10, 1), (10, 2), (10, 3)]
    countX_args = ["xxhixx", "xhixhix", "hi", "h", "x", "", "hihi", "hiAAhi12hi"]
    countHi_args = ["xxhixx", "xhixhix", "hi", "hihih", "h", "", "hiAAhi12hi"]
    changeXY_args = ["codex", "xxhixx", "xhixhix", "hiy", "h", "x", "", "xxx", "yyhxyi", "hihi"]
    changePi_args = ["xpix", "pipi", "pip", "pi", "hip", "p", "x", "", "pixx", "xyzzy"]
    noX_args = ["xaxb", "abc", "xx", "", "axxbxx", "Hellox"]
    array6_args = [([1, 6, 4], 0), ([1, 4], 0), ([6], 0), ([], 0), ([6, 2, 2], 0), ([2, 5], 0), ([1, 9, 4, 6, 6], 0),
                   ([2, 5, 6], 0)]
    array11_args = [([1, 2, 11], 0), ([11, 11], 0), ([1, 2, 3, 4], 0), ([1, 11, 3, 11, 11], 0), ([11], 0), ([1], 0),
                    ([], 0), ([11, 2, 3, 4, 11, 5], 0), ([11, 5, 11], 0)]
    array220_args = [([1, 2, 20], 0), ([3, 30], 0), ([3], 0), ([], 0), ([3, 3, 30, 4], 0), ([2, 19, 4], 0),
                     ([20, 2, 21], 0), ([20, 2, 21, 210], 0), ([2, 200, 2000], 0), ([0, 0], 0), ([2, 4, 40, 5], 0),
                     ([30, 3, 40, 4], 0)]
    allStar_args = ["hello", "abc", "ab", "a", "", "3.14", "Chocolate", "1234"]
    pairStar_args = ["hello", "xxyy", "aaaa", "aaab", "aa", "a", "", "noadjacent", "abba", "abbba"]
    endX_args = ["xxre", "xxhixx", "xhixhix", "hiy", "h", "x", "xx", "", "bxx", "bxax", "axaxax", "xxhxi"]
    countPairs_args = ["axa", "axax", "axbx", "hi", "hihih", "ihihhh", "ihjxhh", "", "a", "aa", "aaa"]
    countAbc_args = ["abc", "abcxxabc", "abaxxaba", "ababc", "abxbc", "aaabc", "hello", "", "ab", "aba", "aca", "aaa"]
    count11_args = ["11abc11", "abc11x11x11", "111", "1111", "1", "", "hi", "11x111x1111", "1x111", "1Hello1", "Hello"]
    stringClean_args = ["yyzzza", "abbbcdd", "Hello", "XXabcYY", "112ab445", "Hello Bookkeeper"]
    countHi2_args = ["ahixhi", "ahibhi", "xhixhi", "hixhi", "hixhhi", "hihihi", "hihihix", "xhihihix", "xxhi", "hixxhi",
                     "hi", "xxxx", "h", "x", "", "Hellohi"]
    parenBit_args = ["xyz(abc)123", "x(hello)", "(xy)1", "not really (possible)", "(abc)", "(x)", "()",
                     "hello(not really)there", "ab(ab)ab"]
    nestParen_args = ["(())", "((()))", "(((x))", "((())", "((()()", "()", "", "(yy)", "(())", "(((y))", "((y)))",
                      "((()))", "(())))", "((yy())))", "(((())))"]
    strCount_args = [("catcowcat", "cat"), ("catcowcat", "cow"), ("catcowcat", "dog"), ("cacatcowcat", "cat"),
                     ("xyx", "x"), ("iiiijj", "i"), ("iiiijj", "ii"), ("iiiijj", "iii"), ("iiiijj", "j"),
                     ("iiiijj", "jj"), ("aaabababab", "ab"), ("aaabababab", "aa"), ("aaabababab", "a"),
                     ("aaabababab", "b")]
    strCopies_args = [("catcowcat", "cat", 2), ("catcowcat", "cow", 2), ("catcowcat", "cow", 1), ("iiijjj", "i", 3),
                      ("iiijjj", "i", 4), ("iiijjj", "ii", 2), ("iiijjj", "ii", 3), ("iiijjj", "x", 3),
                      ("iiijjj", "x", 0), ("iiiiij", "iii", 3), ("iiiiij", "iii", 4), ("ijiiiiij", "iiii", 2),
                      ("ijiiiiij", "iiii", 3), ("dogcatdogcat", "dog", 2)]
    strDist_args = [("catcowcat", "cat"), ("catcowcat", "cow"), ("cccatcowcatxx", "cat"), ("abccatcowcatcatxyz", "cat"),
                    ("xyx", "x"), ("xyx", "y"), ("xyx", "z"), ("z", "z"), ("x", "z"), ("", "z"),
                    ("hiHellohihihi", "hi"), ("hiHellohihihi", "hih"), ("hiHellohihihi", "o"), ("hiHellohihihi", "ll")]

    factorial_ans = [1, 2, 6, 24, 120, 720]
    bunnyEars_ans = [0, 2, 4, 6, 10, 8, 24]
    fibonacci_ans = [0, 1, 1, 2, 3, 5, 8, 13]
    bunnyEars2_ans = [0, 2, 5, 7, 10, 12, 15, 25]
    triangle_ans = [0, 1, 3, 6, 10, 15, 21, 28]
    sumDigits_ans = [9, 13, 3, 1, 1, 0, 10, 4, 5, 3, 10]
    count7_ans = [2, 1, 0, 2, 1, 3, 4, 2, 6, 4, 5, 0, 1]
    count8_ans = [1, 2, 4, 4, 0, 2, 6, 1, 1, 3, 0, 5, 5, 1, 3, 9, 2, 1]
    powerN_ans = [3, 9, 27, 2, 4, 8, 16, 32, 10, 100, 1000]
    countX_ans = [4, 3, 0, 0, 1, 0, 0, 0]
    countHi_ans = [1, 2, 1, 2, 0, 0, 3]
    changeXY_ans = ["codey", "yyhiyy", "yhiyhiy", "hiy", "h", "y", "", "yyy", "yyhyyi", "hihi"]
    changePi_ans = ["x3.14x", "3.143.14", "3.14p", "3.14", "hip", "p", "x", "", "3.14xx", "xyzzy"]
    noX_ans = ["ab", "abc", "", "", "ab", "Hello"]
    array6_ans = [True, False, True, False, True, False, True, True]
    array11_ans = [1, 2, 0, 3, 1, 0, 0, 2, 2]
    array220_ans = [True, True, False, False, True, False, False, True, True, True, True, False]
    allStar_ans = ["h*e*l*l*o", "a*b*c", "a*b", "a", "", "3*.*1*4", "C*h*o*c*o*l*a*t*e", "1*2*3*4"]
    pairStar_ans = ["hel*lo", "x*xy*y", "a*a*a*a", "a*a*ab", "a*a", "a", "", "noadjacent", "ab*ba", "ab*b*ba"]
    endX_ans = ["rexx", "hixxxx", "hihixxx", "hiy", "h", "x", "xx", "", "bxx", "baxx", "aaaxxx", "hixxx"]
    countPairs_ans = [1, 2, 1, 0, 3, 3, 0, 0, 0, 0, 1]
    countAbc_ans = [1, 2, 2, 2, 0, 1, 0, 0, 0, 1, 0, 0]
    count11_ans = [2, 3, 1, 2, 0, 0, 0, 4, 1, 0, 0]
    stringClean_ans = ["yza", "abcd", "Helo", "XabcY", "12ab45", "Helo Bokeper"]
    countHi2_ans = [1, 2, 0, 1, 2, 3, 3, 2, 0, 1, 1, 0, 0, 0, 0, 1]
    parenBit_ans = ["(abc)", "(hello)", "(xy)", "(possible)", "(abc)", "(x)", "()", "(not really)", "(ab)"]
    nestParen_ans = [True, True, False, False, False, True, True, False, True, False, False, True, False, False, True]
    strCount_ans = [2, 1, 0, 2, 2, 4, 2, 1, 2, 1, 4, 1, 6, 4]
    strCopies_ans = [True, False, True, True, False, True, False, False, True, True, False, True, False, True]
    strDist_ans = [9, 3, 9, 12, 3, 1, 0, 1, 0, 0, 13, 5, 1, 2]

    for prob in argv:
        correct = 0  # counts number of test cases passed
        # loop over test cases
        for i in range(len(locals()[prob + "_args"])):
            if (type(locals()[prob + "_args"][i]) is str) or (type(locals()[prob + "_args"][i]) is int) or (
                len(locals()[prob + "_args"][i]) == 1):  # function takes one argument
                if globals()[prob](locals()[prob + "_args"][i]) == locals()[prob + "_ans"][i]:
                    print("\nCorrect!", prob + "(" + str(locals()[prob + "_args"][i]) + ") result:",
                          str(globals()[prob](locals()[prob + "_args"][i])), " expected:",
                          str(locals()[prob + "_ans"][i]))
                    correct += 1
                else:  # print fail message
                    print("\nWrong!", prob + "(" + str(locals()[prob + "_args"][i]) + ") result:",
                          str(globals()[prob](locals()[prob + "_args"][i])), " expected:",
                          str(locals()[prob + "_ans"][i]))
            elif len(locals()[prob + "_args"][i]) == 2:  # there are two arguments to function
                first, second = locals()[prob + "_args"][i]
                if globals()[prob](first, second) == locals()[prob + "_ans"][i]:
                    print("\nCorrect!", prob + "(" + str(locals()[prob + "_args"][i]) + ") result:",
                          str(globals()[prob](first, second)), " expected:", str(locals()[prob + "_ans"][i]))
                    correct += 1
                else:  # print fail message
                    print("\nWrong!", prob + "(" + str(locals()[prob + "_args"][i]) + ") result:",
                          str(globals()[prob](first, second)), " expected:", str(locals()[prob + "_ans"][i]))
            else:
                first, second, third = locals()[prob + "_args"][i]
                if globals()[prob](first, second, third) == locals()[prob + "_ans"][i]:
                    print("\nCorrect!", prob + "(" + str(locals()[prob + "_args"][i]) + ") result:",
                          str(globals()[prob](first, second, third)), " expected:", str(locals()[prob + "_ans"][i]))
                    correct += 1
                else:  # print fail message
                    print("\nWrong!", prob + "(" + str(locals()[prob + "_args"][i]) + ") result:",
                          str(globals()[prob](first, second, third)), " expected:", str(locals()[prob + "_ans"][i]))
        print("\n" + prob + ": passed", correct, "out of", len(locals()[prob + "_ans"]), "\n")


def printHelp():
    print("\nRemove the comment symbol before the name of the function")
    print("that you wish to write and test. Write your code and then")
    print("test your code on the command line. For example, if the")
    print("function that you wrote was factorial, you would test it on")
    print("the command line like so:\n")
    print("python recursion1.py factorial\n")
    print("Invoke with \"python recursion1.py all\" to run all of the")
    print("function tests\n")


import sys

if __name__ == "__main__":
    main(sys.argv[1:])
