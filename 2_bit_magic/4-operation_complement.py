def method1(n: int) -> bin:
    """
    >>> method1(60)
    '-0b111101'
    >>> method1(31)
    '-0b100000'
    >>> method1(-31)
    '0b11110'
    >>> method1(-1231)
    '0b10011001110'
    >>> method1(10)
    '-0b1011
    """
    return bin(~n)

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(60), number=10000)) # 0.0014995479998560768
    """
    import doctest
    doctest.testmod()