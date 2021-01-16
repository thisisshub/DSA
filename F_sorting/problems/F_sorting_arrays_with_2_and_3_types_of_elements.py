def method1(arr: list, n: int) -> list:
    type0 = 0
    type1 = n - 1
    while type0 < type1:
        if arr[type0] == 1:
            arr[type0], arr[type1] = arr[type1], arr[type0]
            type1 -= 1
        else:
            type0 += 1


if __name__ == "__main__":
    """
    arr = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    n = len(arr)
    from timeit import timeit
    print(timeit(lambda: method1(arr, n), number=10000)) # 0.01202381199982483
    """
