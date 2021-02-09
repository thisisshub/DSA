def memoize_factorial(f):
    memory = {}

    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


if __name__ == "__main__":
    """
    from timeit import timeit

    print(timeit(lambda: facto(5), number=10000))  # 0.0009072790053323843
    """