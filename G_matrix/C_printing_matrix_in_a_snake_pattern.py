def method1(n: int, m: int, matrix: list) -> list:
    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                print(str(matrix[i][j]), end=" ")
        else:
            for j in range(n - 1, -1, -1):
                print(str(matrix[i][j]), end=" ")


if __name__ == "__main__":
    from timeit import timeit

    matrix = [[10, 20, 30, 40], [15, 15, 25, 55], [17, 19, 17, 18], [1, 8, 9, 2]]
    print(timeit(lambda: method1(4, 4, matrix), number=10000))  # 0.1679946160002146
