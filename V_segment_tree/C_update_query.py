MAX = 1000


tree = [0] * MAX
lazy = [0] * MAX


def updateRangeUtil(si, ss, se, us, ue, diff):

    if lazy[si] != 0:

        tree[si] += (se - ss + 1) * lazy[si]

        if ss != se:

            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]

        lazy[si] = 0

    if ss > se or ss > ue or se < us:
        return

    if ss >= us and se <= ue:

        tree[si] += (se - ss + 1) * diff

        if ss != se:

            lazy[si * 2 + 1] += diff
            lazy[si * 2 + 2] += diff

        return

    mid = (ss + se) // 2
    updateRangeUtil(si * 2 + 1, ss, mid, us, ue, diff)
    updateRangeUtil(si * 2 + 2, mid + 1, se, us, ue, diff)

    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]


def updateRange(n, us, ue, diff):
    updateRangeUtil(0, 0, n - 1, us, ue, diff)


def getSumUtil(ss, se, qs, qe, si):

    if lazy[si] != 0:

        tree[si] += (se - ss + 1) * lazy[si]

        if ss != se:

            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]

        lazy[si] = 0

    if ss > se or ss > qe or se < qs:
        return 0

    if ss >= qs and se <= qe:
        return tree[si]

    mid = (ss + se) // 2
    return getSumUtil(ss, mid, qs, qe, 2 * si + 1) + getSumUtil(
        mid + 1, se, qs, qe, 2 * si + 2
    )


def getSum(n, qs, qe):

    if qs < 0 or qe > n - 1 or qs > qe:
        print("Invalid Input")
        return -1

    return getSumUtil(0, n - 1, qs, qe, 0)


def constructSTUtil(arr, ss, se, si):

    if ss > se:
        return

    if ss == se:

        tree[si] = arr[ss]
        return

    mid = (ss + se) // 2
    constructSTUtil(arr, ss, mid, si * 2 + 1)
    constructSTUtil(arr, mid + 1, se, si * 2 + 2)

    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]


def constructST(arr, n):

    constructSTUtil(arr, 0, n - 1, 0)


if __name__ == "__main__":
    
    from timeit import timeit

    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)

    constructST(arr, n)

    print(timeit(lambda: updateRange(n, 1, 5, 10), number=10000))  
    