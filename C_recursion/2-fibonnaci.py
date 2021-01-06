def method1(n: int) -> int:
    """
    >>> method1(0)
    0
    >>> method1(1)
    1
    >>> method1(2)
    1
    >>> method1(3)
    2
    >>> method1(4)
    3
    >>> method1(5)
    5
    >>> method1(10)
    55
    """
    return int(((((1+5**.5)/2)**n)-(((1-5**.5)/2)**n))/5**.5)


def method2(n: int) -> int:
    """
    >>> method2(0)
    0
    >>> method2(1)
    1
    >>> method2(2)
    1
    >>> method2(3)
    2
    >>> method2(4)
    3
    >>> method2(5)
    5
    >>> method2(10)
    55
    """
    from functools import reduce
    c = reduce(lambda x, n:[x[1], x[0]+x[1]], range(n), [0, 1])[0]
    return c

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(20), number=10000)) # 0.004012904999399325
    print(timeit(lambda: method2(20), number=10000)) # 0.04924747400036722
    """
    import doctest
    doctest.testmod