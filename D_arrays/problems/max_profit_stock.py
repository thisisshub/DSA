def method1():
    def maxProfit(prices):

        n = len(prices)
        cost = 0
        maxcost = 0

        if n == 0:
            return 0
        min_price = prices[0]
        for i in range(n):
            min_price = min(min_price, prices[i])
            cost = prices[i] - min_price
            maxcost = max(maxcost, cost)
        return maxcost

    prices = [7, 1, 5, 3, 6, 4]
    return maxProfit(prices)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) # 0.020394561999637517
    """
