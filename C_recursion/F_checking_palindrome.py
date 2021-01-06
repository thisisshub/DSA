def method1(n: int) -> bool:
    """
    >>> method1(1111)
    True
    >>> method1(1121)
    False
    """
    return True if str(n)==str(n)[::-1] else False

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(1111), number=10000)) # 0.004767893999087391
    """
    import doctest
    doctest.testmod()
