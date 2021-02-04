def method1():
    def print_well_ordered(number, x, k):
        if k == 0:
            print(number, end=" ")
            return

        for i in range((x + 1), 10):
            print_well_ordered(number * 10 + i, i, k - 1)

    def generate_welL_ordered(k):
        print_well_ordered(0, 0, k)

    k = 3
    return generate_welL_ordered(k)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=100000)) # 19.001043160002155
    """
