def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def insertion_sort(a):
    for i in range(0, len(a)):
        for j in range(i, 0, -1):
            if (a[j] < a[j-1]):
                swap(a, j, j-1)
            else:
                break

def selection_sort(a):
    for i in range(0, len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        swap(a, i, min_index)



if __name__ == "__main__":
    arr = []
    arr.append([3, 4, 1, 21, 5, 1, 7])
    arr.append([13, 521, 12, 4, 14, 55, 13, 5, 11, 52])
    arr.append([])
    arr.append([1])
    arr.append([4, 1])
    arr.append([1, 5])
    arr.append([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    arr.append([1, 3, 2])
    arr.append([1, 1, 1])
    arr.append([0, 0, 0, 0, 0, 0, 0, 0])

    for a in arr:
        print("Before:", a)
        #insertion_sort(a)
        selection_sort(a)
        print("After:", a)