def method1(s, m, n):

    
    
    i, j, count = 0, 0, 0

    
    
    
    
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]:
                count += 1
                break

    
    
    if count >= 1:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    
    from timeit import timeit

    m = 3
    n = 3
    s = [[1, 0, 1], [0, 0, 0], [1, 0, 0]]

    print(timeit(lambda: method1(s, m, n), number=10000))  
    
