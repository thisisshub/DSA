def method1_iterative(n: int, l: list) -> int:
    low = 0
    high = len(l) - 1
    mid = 0
    while low <= high:
        mid = low+(high-low)//2  #Higher values of low and high would add up to give an error so a bit of mathematicl manipulation
        if l[mid] < n:
            low = mid + 1
        elif l[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    """
    n = 9999
    l = [i for i in range(10000)] # [0, 1, 3, ...., 9999]
    from timeit import timeit
    print(timeit(lambda: method1_iterative(l, 0, len(l)-1, n), number=10000)) # 0.03099031199963065
    """
