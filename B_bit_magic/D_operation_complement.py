def method1(n: int) -> bin:
    return bin(~n)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(60), number=10000)) # 0.0014995479998560768
    """
