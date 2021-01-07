def method1(n: int, m: int) -> bin:
    return bin(n ^ m)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(60, 13), number=10000)) # 0.0017356749999635213
    """
