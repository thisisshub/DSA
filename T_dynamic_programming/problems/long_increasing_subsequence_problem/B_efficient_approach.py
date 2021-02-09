# method1 returns length of the longest increasing subsequence
# in arr of size n
def method1(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    method1 = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and method1[i] < method1[j] + 1:
                method1[i] = method1[j] + 1

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, method1[i])

    return maximum



if __name__ == "__main__":
    """
    from timeit import timeit

    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(timeit(lambda: method1(arr), number=10000))  # 0.0482044410018716
    """