def method1(n: int) -> int:
    """
    >>> method1(0)
    0
    >>> method1(1)
    1
    >>> method1(10)
    2
    >>> method1(20)
    2
    >>> method1(30)
    4
    >>> method1(40)
    2
    >>> method1(50)
    3
    """
    c = 0
    while(n):
        c += n & 1
        n >>= 1
    return c


def method2(n: int) -> int:
    """
    >>> method2(0)
    0
    >>> method2(1)
    1
    >>> method2(10)
    2
    >>> method2(20)
    2
    >>> method2(30)
    4
    >>> method2(40)
    2
    >>> method2(50)
    """
    if n == 0: return 0
    else: return (n & 1) + method2(n >> 1)

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(9), number=10000)) # 0.0034751240000332473
    print(timeit(lambda: method2(9), number=10000)) # 0.006590511000013066
    """
    import doctest
    doctest.testmod()