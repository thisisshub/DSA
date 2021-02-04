def method1(ll, ll2, n):
    i = j = 0
    m1 = m2 = -1
    count = 0
    while count < n + 1:
        count += 1
        if i == n:
            m1 = m2
            m2 = ll2[0]
            break
        elif j == n:
            m1 = m2
            m2 = ll[0]
            break
        if ll[i] <= ll2[j]:
            m1 = m2
            m2 = ll[i]
            i += 1
        else:
            m1 = m2
            m2 = ll2[j]
            j += 1
    return (m1 + m2) / 2


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [1, 12, 15, 26, 38]
    ll2 = [2, 13, 17, 30, 45]
    n1 = len(ll)
    n2 = len(ll2)
    print(timeit(lambda: method1(ll, ll2, n1), number=10000)) # 0.011695754000356828
    """
