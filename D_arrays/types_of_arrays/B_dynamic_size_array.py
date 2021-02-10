def method1(n: list):
    return n


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1([1, 2, 3, 4, 5]), number=10000)) 
    
