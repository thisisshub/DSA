def method1(n: int, k: int) -> int:
    if n == 1:
        return 1
    else:
        return (method1(n - 1, k) + k - 1) % n + 1


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(14, 2), number=10000)) 
    
