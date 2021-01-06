def method1(n: int) -> int:
    return 1 if n == 0 or n == 1 else n*method1(n-1)

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(10), number=10000)) # 0.012313627999901655
    """