def method1(n: int) -> int:
    divisors = [d for d in range(2,n//2+1) if n % d == 0]
    return [d for d in divisors if \
            all( d % od != 0 for od in divisors if od != d )]

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(20), number=10000)) # 0.028740440000547096
    """
    import doctest
    doctest.testmod()