def method1(ll: list, n: int) -> int:

    mp = dict()

    for i in range(n):
        if ll[i] in mp.keys():
            mp[ll[i]] += 1
        else:
            mp[ll[i]] = 1

    for x in mp:
        print(x, " ", mp[x])


if __name__ == "__main__":
    
    from timeit import timeit
    ll = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(ll)
    print(timeit(lambda: method1(ll, n), number=10000)) 
    
