def method1(n: int) -> int:
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def method2(n: int) -> int:
    c = 0
    for i in str(n):
        c += int(i)
    return c


def method3(n: int) -> int:
    return sum(map(int, (str(n))))


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(1234), number=10000)) # 0.005289119000735809
    print(timeit(lambda: method2(1234), number=10000)) # 0.006883707001179573
    print(timeit(lambda: method3(1234), number=10000)) # 0.00851047400101379
    """
