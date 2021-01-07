def method1(n: int) -> int:
    return int(((((1 + 5 ** 0.5) / 2) ** n) - (((1 - 5 ** 0.5) / 2) ** n)) / 5 ** 0.5)


def method2(n: int) -> int:
    from functools import reduce

    c = reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]
    return c


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(20), number=10000)) # 0.004012904999399325
    print(timeit(lambda: method2(20), number=10000)) # 0.04924747400036722
    """
