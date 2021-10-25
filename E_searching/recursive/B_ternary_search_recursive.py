def ternary(l, r, key, arr):
    if (r >= l):
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if (arr[mid1] == key):
            return mid1

        if (arr[mid2] == key):
            return mid2

        if (key < arr[mid1]):

            return ternary(l, mid1 - 1, key, arr)

        elif (key > arr[mid2]):
            return ternary(mid2 + 1, r, key, arr)
        else:
            return ternary(mid1 + 1, mid2 - 1, key, arr)

    return "not present"

if __name__ == "__main__":
 '''
    arr=[i for i in range(10000)] # [0, 1, 3, ...., 9999]
    n = 8000
    from timeit import timeit
    print(timeit(lambda: ternary(0, len(arr)-1,n,arr), number=10000)) #0.05205080000000001'''