import sys

INT_MIN = -sys.maxsize - 1


def method1(arr, n, k):
    max_sum = INT_MIN
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
        max_sum = max(current_sum, max_sum)

    return max_sum


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(method1(arr, n, k))

if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(arr, n, k), number=10000)) # 0.03456093000204419
    """
