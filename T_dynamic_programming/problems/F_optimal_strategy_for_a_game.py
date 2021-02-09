def method1(arr, n):

    # Create a table to store
    # solutions of subproblems
    table = [[0 for i in range(n)] for i in range(n)]

    # Fill table using above recursive
    # formula. Note that the table is
    # filled in diagonal fashion
    # from diagonal elements to
    # table[0][n-1] which is the result.
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap

            # Here x is value of F(i + 2, j),
            # y is F(i + 1, j-1) and z is
            # F(i, j-2) in above recursive
            # formula
            x = 0
            if (i + 2) <= j:
                x = table[i + 2][j]
            y = 0
            if (i + 1) <= (j - 1):
                y = table[i + 1][j - 1]
            z = 0
            if i <= (j - 2):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
    return table[0][n - 1]


if __name__ == "__main__":
    """
    from timeit import timeit

    arr1 = [8, 15, 3, 7]
    n = len(arr1)
    print(method1(arr1, n))

    arr2 = [2, 2, 2, 2]
    n = len(arr2)
    print(method1(arr2, n))

    arr3 = [20, 30, 2, 2, 2, 10]
    n = len(arr3)
    print(
        timeit(lambda: method1(arr3, n), number=10000)
    )  # 0.13903403500444256
    """
