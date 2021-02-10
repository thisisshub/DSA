def method1():
    def findWater(arr, n):
        left = [0] * n
        right = [0] * n
        water = 0
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])
        right[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
        for i in range(0, n):
            water += min(left[i], right[i]) - arr[i]
        return water

    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)

    return findWater(arr, n)


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) 
    
