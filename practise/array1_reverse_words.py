"""
Problem: Reverse all the words in a given line.
input - string
output - input strings with reversed words.
"""

"""
for times from 0 to end//2
    swap start and end
    start ++ , end ++
"""
def reverse_range(line, start, end):
    # while start < end
    for _ in range(0, (end-start)//2):
        line[start], line[end-1] = line[end-1], line[start]
        start += 1
        end -= 1

"""
reverse the string from range 0 to string_length
while start_index is < length of string
    get start_index of word
    get end_index of word
    reverse word from start_index to end_index
    start_index = end_index + 1
return string
"""
def reverse_words(line):
    reverse_range(line, 0, len(line))
    start = 0
    end = 0

    while start < len(line):
        while start < len(line) and line[start] == ' ':
            start += 1
            end += 1

        while end < len(line) and line[end] != ' ':
            end += 1

        reverse_range(line, start, end)

        start = end

    return line


if __name__ == "__main__":
    print("".join(reverse_words(list("hello san how are you"))))
    print("".join(reverse_words(list(""))))
    print("".join(reverse_words(list("hey u"))))
    print("".join(reverse_words(list("  u how"))))
