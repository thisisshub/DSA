def number(a, n, p, k):

    a.sort()

    pre = []
    for i in range(n):
        pre.append(0)

    ans = 0
    i = 0

    pre[0] = a[0]

    if pre[0] <= p:
        ans = 1

    for i in range(1, k - 1):
        pre[i] = pre[i - 1] + a[i]

        if pre[i] <= p:
            ans = i + 1

    pre[k - 1] = a[k - 1]

    for i in range(k - 1, n):
        if i >= k:
            pre[i] += pre[i - k] + a[i]

        if pre[i] <= p:
            ans = i + 1

    return ans


if __name__ == "__main__":
    """
    from timeit import timeit

    n = 5
    arr = [2, 4, 3, 5, 7]
    p = 11
    k = 2

    print(timeit(lambda: number(arr, n, p, k), number=10000))  # 0.01322143599827541
    """
