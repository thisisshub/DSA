def method1(n: int) -> int:
    # Single line to find factorial by recursion.
    return 1 if n == 0 or n == 1 else n * method1(n - 1)


def method2(n: int) -> int:
    '''This function returns the factorial 
    by using In-built function.'''

    import math

    return math.factorial(n)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(10), number=10000)) # 0.012027394001052016
    """
