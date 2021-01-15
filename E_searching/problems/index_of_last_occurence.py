def method1(arr, n, x):
    first = -1
    last = -1
    for i in range(0, n):
        if x != arr[i]:
            continue
        if first == -1:
            first = i
        last = i

    if first != -1:
        print("Last Occurrence = ", last)


if __name__ == "__main__":
    """
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
    n = len(arr)
    x = 8
    from timeit import timeit
    print(timeit(lambda: method1(arr, n, x), number=10000)) # 0.08866931500006103
    """
