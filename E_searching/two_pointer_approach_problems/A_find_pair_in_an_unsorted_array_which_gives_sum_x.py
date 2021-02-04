def method1(arr, arr_size, sum):
    s = set()
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if temp in s:
            print(s.add(arr[i]))

def quickSort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quickSort(A, si, pi - 1)
        quickSort(A, pi + 1, ei)


def partition(A, si, ei):
    x = A[ei]
    i = si - 1
    for j in range(si, ei):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        A[i + 1], A[ei] = A[ei], A[i + 1]
    return i + 1
    
def method2(A, arr_size, sum):
    quickSort(A, 0, arr_size - 1)
    l = 0
    r = arr_size - 1
    while l < r:
        if A[l] + A[r] == sum:
            return 1
        elif A[l] + A[r] < sum:
            l += 1
        else:
            r -= 1
    return 0


if __name__ == "__main__":
    """
    A = [1, 4, 45, 6, 10, 8]
    n = 16
    from timeit import timeit
    print(timeit(lambda: method1(A, len(A), n), number=10000)) # 0.007289881999895442
    print(timeit(lambda: method2(A, len(A), n), number=10000)) # 0.046296988999529276
    """
