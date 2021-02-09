def method1(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if wt[n - 1] > W:
        return method1(W, wt, val, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n - 1] + method1(W - wt[n - 1], wt, val, n - 1),
            method1(W, wt, val, n - 1),
        )


if __name__ == "__main__":
    """
    from timeit import timeit

    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(timeit(lambda: method1(W, wt, val, n), number=10000))  # 0.0221543079969706
    """