def method1(arr: list, n: int, x: int) -> int:
    res = 0
    for i in range(n):
        if x == arr[i]:
            res += 1
    return res


if __name__ == "__main__":
    """
    arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
    n = len(arr)
    x = 2
    from timeit import timeit
    print(timeit(lambda: method1(arr, n, x), number=10000)) # 0.009037977999923896
    """
