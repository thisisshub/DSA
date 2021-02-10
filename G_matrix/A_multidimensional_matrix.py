def method1(l: list) -> list:
    l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
    return l


def method2(l: list) -> list:
    l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
    for i in l:
        return i


def method3(l: list) -> list:
    l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
    for i in l:
        for j in i:
            print(j, end=" ")


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(l), number=10000)) 
    print(timeit(lambda: method2(l), number=10000)) 
    print(timeit(lambda: method3(l), number=10000)) 
    
