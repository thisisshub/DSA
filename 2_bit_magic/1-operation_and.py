def method1(n: int, m: int) -> bin:
    """
    >>> method1(25, 30)
    '0b11000'
    >>> method1(76, 30)
    '0b1100'
    >>> method1(60, 13)
    '0b1100
    """
    return bin(n & m)


if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(25, 30), number=10000)) # 0.0016055950000009034
    """
    import doctest
    doctest.testmod()