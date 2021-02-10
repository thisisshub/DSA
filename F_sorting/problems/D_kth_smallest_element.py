def method1(arr, n, k):
    arr.sort()
    return arr[k - 1]


def method2(arr, k):
    import heapq

    smallest = []
    for value in arr:
        if len(smallest) < k:
            heapq.heappush(smallest, -value)
        else:
            heapq.heappushpop(smallest, -value)
    if len(smallest) < k:
        return None
    return -smallest[0]


if __name__ == "__main__":
    
    from timeit import timeit
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print(timeit(lambda: method1(arr, n, k), number=10000))  
    print(timeit(lambda: method2(arr, k), number=10000))  
    
