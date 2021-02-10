def method1(arr, n, x):
    first = -1
    for i in range(0, n):
        if x != arr[i]:
            continue
        if first == -1:
            first = i

    if first != -1:
        print("First Occurrence = ", first)


if __name__ == "__main__":
    
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
    n = len(arr)
    x = 8
    from timeit import timeit
    print(timeit(lambda: method1(arr, n, x), number=10000)) 
    
