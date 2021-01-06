def method1(n: list) -> list:
    """
    >>> method1([1, 2, 3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    x = len(n)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, n) if i & mask]


def method2(n: set) -> list:
    """
    >>> method1({1, 2, 3})
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    from itertools import combinations
    return ([x for i in range(len(n)+1) for x in combinations(n, i)])

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1([1, 2, 3, 4, 5, 6]), number=10000)) # 0.003230058999179164
    print(timeit(lambda: method2({1, 2, 3, 4, 5, 6}), number=10000)) # 0.055786498000088613
    """
    import doctest
    doctest.testmod()