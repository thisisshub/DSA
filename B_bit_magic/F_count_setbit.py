def method1(n: int) -> int:
    c = 0
    while n:
        c += n & 1
        n >>= 1
    return c


def method2(n: int) -> int:
    if n == 0:
        return 0
    else:
        return (n & 1) + method2(n >> 1)


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(9), number=10000)) 
    print(timeit(lambda: method2(9), number=10000)) 
    
