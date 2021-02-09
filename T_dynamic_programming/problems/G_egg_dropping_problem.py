import sys


def eggDrop(n, k):

    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if k == 1 or k == 0:
        return k

    # We need k trials for one egg
    # and k floors
    if n == 1:
        return k

    min = sys.maxsize

    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):

        res = max(eggDrop(n - 1, x - 1), eggDrop(n, k - x))
        if res < min:
            min = res

    return min + 1


if __name__ == "__main__":
    """
    from timeit import timeit

    n = 2
    k = 10
    print(timeit(lambda: eggDrop(n, k), number=10000))  # 2.694228070002282
    """
