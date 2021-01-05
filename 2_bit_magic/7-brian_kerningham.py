def method1(n: int) -> int:
    """
    >>> method1(0)
    0
    >>> method1(1)
    1
    >>> method1(9)
    2
    >>> method1(10)
    2
    >>> method1(20)
    2
    >>> method1(30)
    4
    """
    c = 0
    while n:
        n &= (n-1)
        c += 1
    return c

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(9), number=10000)) # 0.0021619279996230034
    """
    import doctest
    doctest.testmod()