def method1(price, n, S):
    S[0] = 1
    for i in range(1, n, 1):
        S[i] = 1
        j = i - 1
        while (j >= 0) and (price[i] >= price[j]):
            S[i] += 1
            j -= 1


if __name__ == "__main__":
    """
    from timeit import timeit

    price = [10, 4, 5, 90, 120, 80]
    n = len(price)
    S = [None] * n
    print(timeit(lambda: method1(price, n, S), number=10000))  # 0.014990185001806822
    """
