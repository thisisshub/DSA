def methoda(n: int) -> list:
    """
    >>> methoda(10)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    return [i for i in range(n, 0, -1)]


def methodb(n: int) -> list:
    """
    >>> methodb(10)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    return [n - x for x in range(n)]


def methodc(n: int) -> int:
    """
    >>> methodc(10)
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    """
    while n>0:
        print(n)
        n-=1


def methodd(n: int) -> int:
    """
    >>> methodd(10)
    10 9 8 7 6 5 4 3 2 1
    """
    print(*range(n, 0, -1))

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: methoda(10), number=10000)) # 0.005636529000184964
    print(timeit(lambda: methodb(10), number=10000)) # 0.0071275150003202725
    print(timeit(lambda: methodd(10), number=10000)) # 0.062233691998699214
    print(timeit(lambda: methodc(10), number=10000)) # 0.26295897900126874
    """
    import doctest 
    doctest.testmod()