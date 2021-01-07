def method1(n: int, l: list) -> list:
    print(l.insert(4, 8))  # [0, 1, 2, 3, 15, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    """
    n = 15
    l = [i for i in range(10)]
    from timeit import timeit
    print(timeit(lambda: method1(n, l), number=10000)) # 0.011750334000680596
    """
