def method1(ll: list, n: int) -> int:
    maxCount = 0
    index = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if ll[i] == ll[j]:
                count += 1
        if count > maxCount:
            maxCount = count
            index = i
    if maxCount > n // 2:
        print(ll[index])


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [1, 1, 2, 1, 3, 5, 1]
    n = len(ll)
    print(timeit(lambda: method1(ll, n), number=10000)) # 0.09685827199973573
    """
