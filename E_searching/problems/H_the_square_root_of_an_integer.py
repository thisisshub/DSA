def method1(x: int) -> int:
    if x == 0 or x == 1:
        return x
    i = 1
    result = 1
    while result <= x:
        i += 1
        result = i * i
    return i - 1


def method2(x: int) -> int:
    if x == 0 or x == 1:
        return x
    start = 1
    end = x
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid + 1
            ans = mid

        else:
            end = mid - 1

    return ans


if __name__ == "__main__":
    
    from timeit import timeit
    x = 11
    print(timeit(lambda: method1(x), number=10000))  
    print(timeit(lambda: method2(x), number=10000))  
    
