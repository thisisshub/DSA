def method1(l: list):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


if __name__ == "__main__":
    """
    l = [1, 3, 4, 7, 5, 9]
    from timeit import timeit
    print(timeit(method1(l), number=10000)) # 0.013673285000550095
    """
