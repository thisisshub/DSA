def method1(ll: list, n: int) -> int:
    s = set()
    ans = 0
    for ele in ll:
        s.add(ele)
    for i in range(n):
        if (ll[i] - 1) not in s:
            j = ll[i]
            while j in s:
                j += 1
            ans = max(ans, j - ll[i])
    return ans


if __name__ == "__main__":
    """
    from timeit import timeit
    n = 7
    ll = [1, 9, 3, 10, 4, 20, 2]
    print(timeit(lambda: method1(ll, n), number=10000)) # 0.021972083995933644
    """
