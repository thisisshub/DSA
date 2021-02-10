def method1(price: list, n: int) -> int:
    import sys

    if n <= 0:
        return 0
    max_val = -sys.maxsize - 1
    for i in range(0, n):
        max_val = max(max_val, price[i] + method1(price, n - i - 1))
    return max_val


if __name__ == "__main__":
    
    from timeit import timeit
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    print(timeit(lambda: method1(prices, len(prices)), number=10000)) 
    
