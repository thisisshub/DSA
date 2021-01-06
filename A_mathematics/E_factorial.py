def method1(n: int) -> int:
    """
    >>> method1(4)
    24
    >>> method1(3)
    6
    >>> method1(2)
    2
    >>> method1(1)
    1
    >>> method1(0)
    1
    """
    return 1 if n==0 or n==1 else n*method1(n-1)


if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(10), number=10000)) # 0.012027394001052016
    """