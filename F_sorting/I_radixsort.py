def method1(ll: list) -> list:
    def countingSort(arr, exp1):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = arr[i] / exp1
            count[int((index) % 10)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] / exp1
            output[count[int((index) % 10)] - 1] = arr[i]
            count[int((index) % 10)] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def radixSort(arr):
        max1 = max(arr)
        exp = 1
        while max1 / exp > 0:
            countingSort(arr, exp)
            exp *= 10

    return radixSort(ll)


if __name__ == "__main__":
    """
    l = ['1', '3', '4', '7', '5', '9']
    from timeit import timeit
    print(timeit(lambda: method1(l), number=10000)) # 0.002465166999172652
    """
