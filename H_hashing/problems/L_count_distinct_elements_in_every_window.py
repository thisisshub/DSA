from collections import defaultdict


def method1(ll: list, k: int, n: int) -> int:
    mp = defaultdict(lambda: 0)
    dist_count = 0
    for i in range(k):
        if mp[ll[i]] == 0:
            dist_count += 1
        mp[ll[i]] += 1
    print(dist_count)
    for i in range(k, n):
        if mp[ll[i - k]] == 1:
            dist_count -= 1
        mp[ll[i - k]] -= 1
        if mp[ll[i]] == 0:
            dist_count += 1
        mp[ll[i]] += 1
        print(dist_count)


if __name__ == "__main__":
    
    from timeit import timeit
    ll = [1, 2, 1, 3, 4, 2, 3]
    n = len(ll)
    k = 4
    print(timeit(lambda: method1(ll, k, n), number=10000)) 
    
