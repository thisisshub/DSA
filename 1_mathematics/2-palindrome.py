def method1(n: str) -> bool:
    '''
    >>> method1('aibohphobia')
    True
    >>> method1('string')
    False
    '''
    return True if n==n[::-1] else False

if __name__ == '__main__':
    '''
    from timeit import timeit
    print(timeit(lambda: method1('aibohphobia'), number=10000))
    '''
    import doctest
    doctest.testmod()