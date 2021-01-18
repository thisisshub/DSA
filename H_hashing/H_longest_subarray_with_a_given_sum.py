def method1(ll: list, n: int, k: int):
    mydict = dict()
    sum = 0
    maxLen = 0
    for i in range(n):
        sum += ll[i]
        if sum == k:
            maxLen = i + 1
        elif (sum - k) in mydict:
            maxLen = max(maxLen, i - mydict[sum - k])
        if sum not in mydict:
            mydict[sum] = i
    return maxLen


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [10, 5, 2, 7, 1, 9]
    n = len(ll)
    k = 15
    print(timeit(lambda: method1(ll, n, k), number=10000)) # 0.01679191100265598
    """
