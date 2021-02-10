def method1(n: int, l: list) -> list:
    n = 2
    l = [i for i in range(10)]  
    return l.remove(2)  


def method2(n: int, l: list) -> list:
    n = 2
    l = [i for i in range(10)]  
    return l.pop(0)  


if __name__ == "__main__":
    
    n = 2
    l = [i for i in range(10)] 
    from timeit import timeit
    print(timeit(lambda: method1(n, l), number=10000)) 
    print(timeit(lambda: method2(n, l), number=10000)) 
    
