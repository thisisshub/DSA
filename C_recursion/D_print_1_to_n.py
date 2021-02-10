def method1(n: int) -> list:
    return [i for i in range(1, n + 1)]


def method2(n: int) -> int:
    i = 1
    while i <= n:
        print(i)
        i += 1


def method3(n: int) -> int:
    print(*range(1, n + 1))


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(10), number=10000)) 
    print(timeit(lambda: method2(10), number=10000)) 
    print(timeit(lambda: method3(10), number=10000)) 
    
