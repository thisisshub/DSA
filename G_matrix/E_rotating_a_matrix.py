def method1():
    N = 4

    
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    def rotateMatrix(mat):
        for x in range(0, int(N / 2)):
            for y in range(x, N - x - 1):
                temp = mat[x][y]
                mat[x][y] = mat[y][N - 1 - x]
                mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
                mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
                mat[N - 1 - y][x] = temp

    def displayMatrix(mat):
        for i in range(0, N):
            for j in range(0, N):
                print(mat[i][j], end=" ")
            print("")
        return rotateMatrix(mat)

    return (rotateMatrix(mat), displayMatrix(mat))


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) 
    
