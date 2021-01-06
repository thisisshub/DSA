def methoda(n: int, m: int) -> int:
    """
    >>> methoda(2, 3)
    6
    >>> methoda(-2, -3)
    6
    >>> methoda(2, -3)
    6
    >>> methoda(-2, 3)
    6
    """
    def gcd(n: int, m: int) -> int:
        while m:
            n, m = m, n%m
        return n
    return abs((n*m)//gcd(n, m))


def methodb(n: int, m: int) -> int:
    """
    >>> methodb(2, 3)
    6
    >>> methodb(-2, -3)
    6
    >>> methodb(2, -3)
    6
    >>> methodb(-2, 3)
    6
    """
    from math import gcd
    return abs(n*m)//gcd(n, m)

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: methoda(2, 3), number=10000)) # 0.0052234140021028
    print(timeit(lambda: methodb(2, 3), number=10000)) # 0.010972605999995722
    """
    import doctest
    doctest.testmod()