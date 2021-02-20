def binary_search(numbers, key):
    low = 0
    high = len(numbers) - 1

    while (low <= high):
        mid = low + (high-low)//2
        #print('low %d mid %d high %d' % (low, mid, high))
        val = int(numbers[mid])
        #print(key, val)
        if key == val:
            return mid
        elif key < val:
            high = mid - 1
        else:
            low = mid + 1

    return None

def test_binary_search():
    numbers = input(' Enter number in sorted fashion: ').split()
    key = input('Enter search value: ')

    index = binary_search(numbers, int(key))

    if index is None:
        print("Key not found")
    else:
        print("Key found at index:", index)

if __name__ == '__main__':
    test_binary_search()

