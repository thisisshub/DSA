

def method1(arr):
    n = len(arr)

    
    
    method1 = [1] * n

    
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and method1[i] < method1[j] + 1:
                method1[i] = method1[j] + 1

    
    
    maximum = 0

    
    for i in range(n):
        maximum = max(maximum, method1[i])

    return maximum



if __name__ == "__main__":
    
    from timeit import timeit

    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(timeit(lambda: method1(arr), number=10000))  
    