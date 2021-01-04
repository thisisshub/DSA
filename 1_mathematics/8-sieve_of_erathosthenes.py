def method1(n: int) -> int:
    """
    >>> method1(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> method1(0)
    []
    >>> method1(1)
    []
    >>> method1(2)
    []
    >>> method1(3)
    [2]
    """
    if n <= 2: return []
    else: 
        sieve = [True] * (n + 1)
        for x in range(3, int(n**0.5)+1, 2):
            for y in range(3, (n//x)+1, 2):
                sieve[(x * y)] = False
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(20), number=10000)) # 0.015664431000914192
    """
    import doctest
    doctest.testmod()