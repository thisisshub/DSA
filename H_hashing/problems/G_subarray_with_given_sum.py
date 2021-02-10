def method1(ll: list, n: int, sum: int) -> int:
    curr_sum = ll[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - ll[start]
            start += 1
        if curr_sum == sum:
            print("Sum found between indexes")
            print("% d and % d" % (start, i - 1))
            return 1
        if i < n:
            curr_sum = curr_sum + ll[i]
        i += 1
    print("No subarray found")
    return 0


if __name__ == "__main__":
    
    from timeit import timeit
    ll = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(ll)
    sum = 23
    print(timeit(lambda: method1(ll, n, sum), number=10000)) 
    
