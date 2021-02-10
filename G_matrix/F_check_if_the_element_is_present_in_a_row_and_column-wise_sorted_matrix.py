def method1():
    def search(mat, n, x):
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

    mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]

    return search(mat, 4, 29)


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) 
    
