import sys



def max(a, b):
    return a if (a > b) else b




def cutRod(price, n):
    if n <= 0:
        return 0
    max_val = -sys.maxsize - 1

    
    
    for i in range(0, n):
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    return max_val


if __name__ == "__main__":
    
    from timeit import timeit

    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print(timeit(lambda: cutRod(arr, size), number=10000))  
    
