def method1(n: list) -> list:
    n = [None] * 5
    return n

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1([None] * 5), number=10000)) # 0.0020053009998264315
    """