'''
Sort a disk file of numbers on a system with limited memory.

input:  File containing numbers with the max of 1billion.
output: File containing sorted numbers of the input
constraints:    Max 128mb of space available

algo:
    Allocate memory for a Bitmap of 128mb which can store 1billion numbers
    Read the file line by line extracting one number at a time and set the bit
    Read the bitmap and write out the corresponding number to output file if set    
datastructure:

    bitmap: list/array of 1billion/bits_per_word, bits_per_word = 32/64

implementation details:
    supporting functions: 
        setbit(bitmap, number)  : set a particular bit to 1
        clrbit(bitmap, number)  : set a particular bit to 0
        testbit(bitmap, number) : check if a bit is set to 1

    main:
        create bitmap
        read infile
            setbits
        create outfile
            write numbers in sorted order
'''

def setbit(bitmap, number):
    print(number//nums_per_word)
    bitmap[number//nums_per_word] \
        = bitmap[number//nums_per_word] | 0x1 << (number % nums_per_word)

def testbit(bitmap, number):
    if (bitmap[number//nums_per_word] & (0x1 << (number % nums_per_word))):
        return 1
    return 0

infile = open("disksort_file", 'r')
outfile = open("disksort_file_sorted", 'w')
numbers = infile.readlines()

biggestnum = 1024*1024*1024*10
nums_per_word = 64

bitmap = [0 for x in range(int(biggestnum//nums_per_word)+1)]
print(len(bitmap))
for num in numbers:
    print(num)
    setbit(bitmap, int(num))

for num in range(0, biggestnum):
    if (num%100000000 == 0) : print("hitting 100000000", num)
    if testbit(bitmap, num):
        outfile.write(str(num))
        outfile.flush()

infile.close()
outfile.close()
