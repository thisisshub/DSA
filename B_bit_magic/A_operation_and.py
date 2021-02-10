def method1(n: int, m: int) -> bin:
    return bin(n & m)


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(25, 30), number=10000)) 
    
