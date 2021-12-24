def method1(price, n, S):
    """
    An algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
    The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.
    For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
    """
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
