def findPeakUtil(ll: list, low: int, high: int, n: int) -> list:
    mid = low + (high - low) / 2
    mid = int(mid)
    if (mid == 0 or ll[mid - 1] <= ll[mid]) and (
        mid == n - 1 or ll[mid + 1] <= ll[mid]
    ):
        return mid
    elif mid > 0 and ll[mid - 1] > ll[mid]:
        return findPeakUtil(ll, low, (mid - 1), n)
    else:
        return findPeakUtil(ll, (mid + 1), high, n)


def method1(ll, n):
    return findPeakUtil(ll, 0, n - 1, n)


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [1, 3, 20, 4, 1, 0]
    n = len(ll)
    print(timeit(lambda: method1(ll, n))) # 0.4230448450007316
    """
