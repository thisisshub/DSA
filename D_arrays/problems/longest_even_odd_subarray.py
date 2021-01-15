def method1(arr: list, n: int) -> list:
    longest = 1
    cnt = 1
    for i in range(n - 1):
        if (arr[i] + arr[i + 1]) % 2 == 1:
            cnt = cnt + 1
        else:
            longest = max(longest, cnt)
            cnt = 1
    if longest == 1:
        return 0
    return max(cnt, longest)


if __name__ == "__main__":
    """
    arr = [ 1, 2, 3, 4, 5, 7, 8 ]
    n = len(arr)
    from timeit import timeit
    print(timeit(lambda: method1(arr, n), number=10000)) # 0.01877671800320968
    """
