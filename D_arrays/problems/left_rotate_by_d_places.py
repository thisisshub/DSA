def method1():
    def method_rotate(arr, n):
        temp = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = temp

    def method(arr: list, d: int, n: int) -> list:
        for _ in range(d):
            method_rotate(arr, n)

    def method_print(arr, n):
        for i in range(n):
            print(arr[i], end=" ")

    arr = [1, 2, 3, 4, 5, 6, 7]
    method(arr, 2, 7)
    return method_print(arr, 7)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) # 0.08287155000016355
    """