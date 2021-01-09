def method1():
    def printBoundary(a, m, n):
        for i in range(m):
            for j in range(n):
                if i == 0:
                    print(a[i][j]),
                elif i == m - 1:
                    print(a[i][j]),
                elif j == 0:
                    print(a[i][j]),
                elif j == n - 1:
                    print(a[i][j]),
                else:
                    print(" "),
            print()

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]
    return printBoundary(a, 4, 4)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) # 0.8269144149999192
    """
