def method1(arr, n, k):
    max = 0

    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        return str(max) + " "


if __name__ == "__main__":
    """
    from timeit import timeit

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3
    print(timeit(lambda: method1(arr, n, k))) # 0.7219209800023236
    """
