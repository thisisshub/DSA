def method1(l: list) -> list:
    n = len(l)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


if __name__ == "__main__":
    """
    l = [1, 3, 4, 7, 5, 9]
    from timeit import timeit
    timeit(lambda: method1(l), number=10000) # 0.02512622900030692
    """
