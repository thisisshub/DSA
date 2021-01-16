def method1(ll1, ll2):
    m = ll1[-1]
    n = ll2[-1]
    ans = 0

    if m > n:
        ans = m
    else:
        ans = n

    newtable = [0] * (ans + 1)
    print(ll1[0], end=" ")
    newtable[ll1[0]] += 1
    for i in range(1, len(ll1)):
        if ll1[i] != ll1[i - 1]:
            print(ll1[i], end=" ")
            newtable[ll1[i]] += 1
    for j in range(0, len(ll2)):
        if newtable[ll2[j]] == 0:
            print(ll2[j], end=" ")
            newtable[ll2[j]] += 1


if __name__ == "__main__":
    """
    from timeit import timeit
    ll1 = [1, 2, 2, 2, 3]
    ll2 = [2, 3, 4, 5]
    print(timeit(lambda: method1(ll1, ll2), number=10000)) # 0.05352691199914261
    """
