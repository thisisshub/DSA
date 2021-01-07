def method1(n: int) -> int:
    return len(str(n)) if n >= 0 else len(str(n)) - 1


def method2(n: int) -> int:
    import math

    return int(math.log10(n) + 1 if n > 0 else (1 if n == 0 else math.log10(-n) + 1))


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(1234567890), number=10000)) # 0.0022839140001451597
    print(timeit(lambda: method2(1234567890), number=10000)) # 0.004222848001518287
    """
