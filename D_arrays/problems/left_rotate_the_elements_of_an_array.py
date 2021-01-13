def method1():
    a = [1, 2, 3, 4, 5]
    for _ in range(1):
        f = a[0]
        for j in range(0, len(a) - 1):
            a[j] = a[j + 1]
        a[len(a) - 1] = f
    return a


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) 0.008410404003370786
    """
