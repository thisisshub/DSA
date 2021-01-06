def method1(n: int) -> list:
    """
    >>> method1(10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return [i for i in range(1, n+1)]


def method2(n: int) -> int:
    """
    >>> method2(10)
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


def method3(n: int) -> int:
    """
    >>> method3(10)
    1 2 3 4 5 6 7 8 9 10
    """
    print(*range(1, n+1))

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(10), number=10000)) # 0.00660862100085069
    print(timeit(lambda: method2(10), number=10000)) # 0.3217459139996208
    print(timeit(lambda: method3(10), number=10000)) # 0.3245184600000357
    """
    import doctest 
    doctest.testmod()