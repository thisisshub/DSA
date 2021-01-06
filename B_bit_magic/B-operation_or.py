def method1(n: int, m: int) -> bin:
    """
    >>> method1(60, 13)
    '0b111101'
    >>> method1(70, 23)
    '0b1010111'
    >>> method1(25, 32)
    '0b111001'
    >>> method1(10, 11)
    '0b1011'
    >>> method1(1, 0)
    '0b1'
    """
    return bin(n | m)


if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(25, 30), number=10000)) # 0.0016012300000056712
    """
    import doctest
    doctest.testmod()