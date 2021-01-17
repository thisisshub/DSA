def method1(mat, n, x):
    i = 0
    j = n - 1
    while i < n and j >= 0:
        if mat[i][j] == x:
            print("n Found at ", i, ", ", j)
            return 1
        if mat[i][j] > x:
            j -= 1
        else:
            i += 1
    print("Element not found")
    return 0


if __name__ == "__main__":
    """
    from timeit import timeit
    mat = [ [10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50] ]
    print(timeit(lambda: method1(mat, 4, 29), number=10000)) # 0.3365673150001385
    """
