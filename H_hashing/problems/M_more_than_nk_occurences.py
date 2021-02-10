def method1(ll: list, n: int, k: int) -> int:
    x = n // k
    freq = {}
    for i in range(n):
        if ll[i] in freq:
            freq[ll[i]] += 1
        else:
            freq[ll[i]] = 1
    for i in freq:
        if freq[i] > x:
            print(i)


if __name__ == "__main__":
    
    from timeit import timeit
    ll = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
    n = len(ll)
    k = 4
    print(timeit(lambda: method1(ll, n, k), number=10000))  
    
