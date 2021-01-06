def method1(n: int, m: int) -> bin:
    """
    >>> method1(60, 13)
    '0b110001'
    >>> method1(70, 13)
    '0b1001011'
    >>> method1(70, 25)
    '0b1011111'
    >>> method1(10, 11)
    '0b1'
    """
    return bin(n ^ m)

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(60, 13), number=10000)) # 0.0017356749999635213
    """
    import doctest
    doctest.testmod()