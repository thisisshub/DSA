def method1(s, f):
    n = len(f)
    print("The following activities are selected")

    i = 0
    print(i, end=" ")

    for j in range(n):

        if s[j] >= f[i]:
            print(j, end=" ")
            i = j


if __name__ == "__main__":
    
    from timeit import timeit

    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print(timeit(lambda: method1(s, f), number=10000))  
    
