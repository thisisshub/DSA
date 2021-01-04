def method1(n: str) -> int:
    '''
    >>> method1(1234567890)
    10
    >>> method1(-1234567890) # answer should be 10
    11
    >>> method1(0)
    1
    '''
    return len(str(n))

def method2(n: int) -> int:
    '''
    >>> method2(1234567890)
    10
    >>> method2(-1234567890)
    10
    >>> method2(0)
    1
    '''
    import math
    return (int(math.log10(n)+1 if n>0 else(1 if n==0 else math.log10(-n)+1)))

if __name__ == '__main__':
    '''
    from timeit import timeit
    print(timeit(lambda: method1(1234567890), number=10000)) # works only for +ve int
    print(timeit(lambda: method2(1234567890), number=10000)) # works for -ve +ve int
    '''
    import doctest
    doctest.testmod()