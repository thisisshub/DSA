def method1(n: int, source: str, destination: str, auxiliary: str) -> str:
    """
    >>> method1(3, 'a', 'b', 'c')
    Move disk 1 from source a to destination b
    Move disk 2 from source a to destination c
    Move disk 1 from source b to destination c
    Move disk 3 from source a to destination b
    Move disk 1 from source c to destination a
    Move disk 2 from source c to destination b
    Move disk 1 from source a to destination b
    """
    if n == 1: print('Move disk 1 from source', source, 'to destination', destination); return
    method1(n - 1, source, auxiliary, destination)
    print('Move disk', n, 'from source', source, 'to destination', destination)
    method1(n - 1, auxiliary, destination, source)

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(3, 'a', 'b', 'c'), number=10000)) # 1.687103215001116
    """
    import doctest
    doctest.testmod()