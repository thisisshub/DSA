def method1(l: list) -> list:
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)

    def printArray(arr, size):
        for i in range(size):
            print(arr[i], end=" ")
        print()

    n = len(l)
    return printArray(l, n)


if __name__ == "__main__":
    """
    l = [1, 3, 4, 7, 5, 9]
    from timeit import timeit
    print(timeit(method1(l), number=10000))  # 0.013673285000550095
    """
