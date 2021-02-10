def method1(arr: list, low: int, high: int) -> int:

    if high >= low:
        mid = low + (high - low) // 2
        if (mid == high or arr[mid + 1] == 0) and (arr[mid] == 1):
            return mid + 1
        if arr[mid] == 1:
            return method1(arr, (mid + 1), high)

        return method1(arr, low, mid - 1)

    return 0


if __name__ == "__main__":
    
    arr=[1, 1, 1, 1, 0, 0, 0]
    from timeit import timeit
    print(timeit(lambda: method1(arr, 0, len(arr)-1), number=10000)) 
    
