matrix = [[1, 2, 3], [4, 5, 6]]


def method1(matrix: list) -> list:
    return matrix


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(matrix), number=10000)) # 0.002698033000342548
    """
