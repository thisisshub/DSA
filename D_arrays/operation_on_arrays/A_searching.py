def method1(l: list, low: int, high: int, x: int) -> int:
    if high >= low:
        mid = (high + low) // 2
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            return method1(l, low, mid - 1, x)
        else:
            return method1(l, mid + 1, high, x)
    else:
        return -1
    return method1(l, 0, len(l) - 1, x)


def method2(n: int, l: list) -> bool:
    return True if l.index(n) <= len(l) else False


def method3(n: int, l: list) -> bool:
    return True if n in l else False


if __name__ == "__main__":
    
    n = 9999
    l = [i for i in range(10000)] 
    from timeit import timeit
    print(timeit(lambda: method1(l, 0, len(l)-1, n), number=10000)) 
    print(timeit(lambda: method2(n, l), number=10000)) 
    print(timeit(lambda: method3(n, l), number=10000)) 
    
