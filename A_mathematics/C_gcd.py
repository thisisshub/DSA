def method1(n: int, m: int) -> int:
    while m:
        n, m = m, n%m
    return abs(n)


def method2(n: int, m: int) -> int:
    from math import gcd
    return gcd(n, m)


if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(3, 9), number=10000)) # 0.0018165660003433004
    print(timeit(lambda: method2(3, 9), number=10000)) # 0.006539128997246735
    """