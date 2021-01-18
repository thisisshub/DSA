def method1(ll: list, n: int) -> int:
    s = set()
    c = 0
    for i in range(n):
        if ll[i] not in s:
            s.add(ll[i])
            c += 1
    return c


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [6, 10, 5, 4, 9, 120, 4, 6, 10]
    n = len(ll)
    print(timeit(lambda: method1(ll, n), number=10000)) # 0.01385382900480181
    """
