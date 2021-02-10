def method1():
    matrix = [[1, 2, 3], [4, 5, 6], [8, 9, 0]]

    ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(matrix)):
        for j in range(3):
            ans[j][i] = matrix[i][j]

    for r in ans:
        print(r)


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) 
    
