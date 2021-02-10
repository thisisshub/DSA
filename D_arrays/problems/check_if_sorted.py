def method1(ll: list, n: int) -> bool:
    import sys

    minEle = sys.maxsize
    minIndex = -1
    for i in range(n):
        if ll[i] < minEle:
            minEle = ll[i]
            minIndex = i
    flag1 = 1
    for i in range(1, minIndex):
        if ll[i] < ll[i - 1]:
            flag1 = 0
            break
    flag2 = 2
    for i in range(minIndex + 1, n):
        if ll[i] < ll[i - 1]:
            flag2 = 0
            break
    return True if (flag1 and flag2 and ll[n - 1] < ll[0]) else False


if __name__ == "__main__":
    
    from timeit import timeit
    ll = [3, 4, 5, 1, 2]
    n = len(ll)
    print(timeit(lambda: method1(ll, n), number=10000)) 
    
