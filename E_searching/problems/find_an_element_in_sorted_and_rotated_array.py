def method1(l: list, n: int, key: int) -> int:
    pivot = findPivot(l, 0, n - 1)
    if pivot == -1:
        return binarySearch(l, 0, n - 1, key)
    if l[pivot] == key:
        return pivot
    if l[0] <= key:
        return binarySearch(l, 0, pivot - 1, key)
    return binarySearch(l, pivot + 1, n - 1, key)


def findPivot(l, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((low + high) / 2)
    if mid < high and l[mid] > l[mid + 1]:
        return mid
    if mid > low and l[mid] < l[mid - 1]:
        return mid - 1
    if l[low] >= l[mid]:
        return findPivot(l, low, mid - 1)
    return findPivot(l, mid + 1, high)


def binarySearch(l, low, high, key):
    if high < low:
        return -1
    mid = int((low + high) / 2)
    if key == l[mid]:
        return mid
    if key > l[mid]:
        return binarySearch(l, (mid + 1), high, key)
    return binarySearch(l, low, (mid - 1), key)


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    n = len(ll)
    key = 3
    print(timeit(lambda: method1(ll, n, key))) # 1.2764019470005223
    """
