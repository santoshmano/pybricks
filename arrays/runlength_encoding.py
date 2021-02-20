"""
Run length encoding and decoding
"""

def runlength_encoding(arr):

    rle = []
    arr_idx = 0

    while arr_idx < len(arr):

        repeat_idx = arr_idx + 1
        while (repeat_idx < len(arr)) and (arr[repeat_idx] == arr[arr_idx]):
            repeat_idx += 1

        if repeat_idx > arr_idx+1:
            rle.append(chr(126 + (repeat_idx-arr_idx)))

        rle.append(arr[arr_idx])
        arr_idx = repeat_idx

    return "".join(rle)


def runlength_decoding(arr):
   rld = []
   arr_idx = 0

   while arr_idx < len(arr):

        if ord(arr[arr_idx]) > 126:
            repeat_num = ord(arr[arr_idx]) - 126 + 1
            while repeat_num-1:
                rld.append(arr[arr_idx+1])
                repeat_num -= 1
            arr_idx += 2
        else:
            rld.append(arr[arr_idx])
            arr_idx += 1

   return "".join(rld)


print(runlength_encoding("abc"))
print(runlength_decoding(runlength_encoding("aabc")))
print(runlength_encoding("aabbcc"))
print(runlength_decoding(runlength_encoding("aaaaabc")))
print(runlength_encoding("aaccccc"))
print(runlength_encoding("aac234cc"))
print(runlength_encoding("a0000ac234cc"))
print(runlength_decoding(runlength_encoding("aac3211222234cc")))

print(runlength_encoding("a12BBBB"))

print(runlength_decoding(runlength_encoding("AAA")))