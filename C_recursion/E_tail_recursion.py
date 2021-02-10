
last operation of a function is a recursive call. 


def tailrecursive(n: int, a=1) -> int:
    if n == 0:
        return a
    return tailrecursive(n - 1, n * a)


def nontailrecursive(n: int) -> int:
    
    
    
    
    
    
    if n == 0:
        return 1
    return n * nontailrecursive(n - 1)


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: tailrecursive(10), number=10000)) 
    print(timeit(lambda: nontailrecursive(10), number=10000)) 
    
