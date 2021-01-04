def method1(n: int, m: int) -> int:
    """
    >>> method1(-123, -321)
    3
    >>> method1(123, 321)
    3
    >>> method1(-123, -321)
    3
    >>> method1(-123, 321)
    3
    >>> method1(123, -321)
    3
    """
    while m:
        n, m = m, n%m
    return abs(n)


def method2(n: int, m: int) -> int:
    """
    >>> method2(123, 321)
    3
    >>> method2(-123, -321)
    3
    >>> method2(-123, 321)
    3
    >>> method2(123, -321)
    3
    """
    from math import gcd
    return gcd(n, m)


if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method2(3, 9), number=10000))
    print(timeit(lambda: method1(3, 9), number=10000))
    """
    import doctest
    doctest.testmod()