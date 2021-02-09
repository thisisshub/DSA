def method1(arr, l, h):

    # Base case: when source and
    # destination are same
    if h == l:
        return 0

    # when nothing is reachable
    # from the given source
    if arr[l] == 0:
        return float("inf")

    # Traverse through all the points
    # reachable from arr[l]. Recursively
    # get the minimum number of jumps
    # needed to reach arr[h] from
    # these reachable points.
    min = float("inf")
    for i in range(l + 1, h + 1):
        if i < l + arr[l] + 1:
            jumps = method1(arr, i, h)
            if jumps != float("inf") and jumps + 1 < min:
                min = jumps + 1

    return min


if __name__ == "__main__":
    """
    from timeit import timeit

    arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
    n = len(arr)
    print(timeit(lambda: method1(arr, 0, n - 1), number=10000))  # 0.7700862489946303
    """