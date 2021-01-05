def methoda(n: int) -> list:
    """
    >>> methoda(10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return [i for i in range(1, n+1)]


def methodc(n: int) -> int:
    """
    >>> methodc(10)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    """
    i = 1
    while i<=n:
        print(i)
        i+=1


def methodd(n: int) -> int:
    """
    >>> methodd(10)
    1 2 3 4 5 6 7 8 9 10
    """
    print(*range(1, n+1))

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: methoda(10), number=10000)) # 0.00660862100085069
    print(timeit(lambda: methodd(10), number=10000)) # 0.3245184600000357
    print(timeit(lambda: methodc(10), number=10000)) # 0.3217459139996208
    """
    import doctest 
    doctest.testmod()