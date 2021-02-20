"""
Digits to Literal representation

i/p : an integer
o/p :string

questions:
    only pos? or pos&neg
    max num? implement till 999?

examples:
1 = One
19 = Nineteen
10, 20, 30, 40, 50, 60 = Ten
21 = Twenty One
44 = Forty Four
100 = One Hundred
120 = One Hundred Twenty

1001 = One thousand and one
12023 = Twelve thousand and twenty three



observations:
    numbers <20 are uniques
    tens are unique
    hundreds, thousands

"""


def _dtol(num):
    """
    num is non zero positive number
    """

    result = ""

    num_map = {
        1:  "One",
        2:  "Two",
        3:  "Three",
        4:  "Four",
        5:  "Five",
        6:  "Six",
        7:  "Seven",
        8:  "Eight",
        9:  "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"}

    num_map_thousands = ["Thousand", "Million", "Billion"]

    count = 0
    result = str()
    while num:
        triplet = num%1000
        num = num//1000

        if triplet in num_map:
            result = num_map[triplet] + " " + result
        else:
            digit = triplet % 10
            if digit: result = num_map[digit] + " " + result

            tens = (triplet % 100) - digit
            if tens: result = num_map[tens] + " " + result

            hundreds = (triplet - tens)//100
            if hundreds: result = num_map[hundreds] + " Hundred " + result

        if num and num%1000:
            result = num_map_thousands[count] + " " + result
        count += 1

    return result

def dtol(num):
    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negative " + _dtol(-num)
    else:
        return _dtol(num)

def test_digit_to_literal():
##    assert(dtol() == "One")

    testnums = [0,
                -1,
                -123,
                999,
                12,
                99,
                100,
                200,
                20,
                123456,
                1000000,
                3400000000]
    for num in testnums:
        print(num, ":", dtol(num))

if __name__ == "__main__":
    test_digit_to_literal()
