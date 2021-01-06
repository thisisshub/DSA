def method1(n: int) -> int:
    c = 0
    while n:
        n &= (n-1)
        c += 1
    return c

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(9), number=10000)) # 0.0021619279996230034
    """