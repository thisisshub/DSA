import sys

# A utility function to get the
# maximum of two integers
def max(a, b):
    return a if (a > b) else b


# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces
def cutRod(price, n):
    if n <= 0:
        return 0
    max_val = -sys.maxsize - 1

    # Recursively cut the rod in different pieces
    # and compare different configurations
    for i in range(0, n):
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    return max_val


if __name__ == "__main__":
    """
    from timeit import timeit

    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print(timeit(lambda: cutRod(arr, size), number=10000))  # 0.7375893329954124
    """
