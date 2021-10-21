def method1(l: list, low: int, high: int, x: int) -> int:
    if high >= low:  #check the is high no is greater than low
        mid = (high + low) // 2   #find mid by taking avg of high & low
        if l[mid] == x:     #check the mid no is equal to finding no
            return mid      # if equal return mid no
        elif l[mid] > x:    # if mid is greater than X
            return method1(l, low, mid - 1, x)      # set high = mid-1
        else:
            return method1(l, mid + 1, high, x)     # set low = mid+1
    else:
        return -1
    return method1(l, 0, len(l) - 1, x)


def method2(n: int, l: list) -> bool:
    return True if l.index(n) <= len(l) else False


def method3(n: int, l: list) -> bool:
    return True if n in l else False


if __name__ == "__main__":
    """
    n = 9999
    l = [i for i in range(10000)] # [0, 1, 3, ...., 9999]
    from timeit import timeit
    print(timeit(lambda: method1(l, 0, len(l)-1, n), number=10000)) # 0.03099031199963065
    print(timeit(lambda: method2(n, l), number=10000)) # 0.9109301280004729
    print(timeit(lambda: method3(n, l), number=10000)) # 0.8249549619995378
    """
