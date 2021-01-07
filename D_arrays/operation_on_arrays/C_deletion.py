def method1(n: int, l: list) -> list:
    n = 2
    l = [i for i in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return l.remove(2)  # [0, 1, 3, 4, 5, 6, 7, 8, 9]


def method2(n: int, l: list) -> list:
    n = 2
    l = [i for i in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return l.pop(0)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    """
    n = 2
    l = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    from timeit import timeit
    print(timeit(lambda: method1(n, l), number=10000)) # 0.007390202999886242
    print(timeit(lambda: method2(n, l), number=10000)) # 0.0074160020012641326
    """
