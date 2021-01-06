"""A special form of recursion where the 
last operation of a function is a recursive call. """

def tailrecursive(n: int, a = 1) -> int:
    if (n == 0): return a
    return tailrecursive(n - 1, n * a)


def nontailrecursive(n: int) -> int:
    # The function is not tail
    # recursive because the value 
    # returned by nontailrecursive(n-1) is used
    # in nontailrecursive(n) and call to nontailrecursive(n-1)
    # is not the last thing done by
    # nontailrecursive(n)
    if n == 0: return 1
    return n * nontailrecursive(n - 1)

if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: tailrecursive(10), number=10000)) # 0.012317868999161874
    print(timeit(lambda: nontailrecursive(10), number=10000)) # 0.010385317998952814
    """