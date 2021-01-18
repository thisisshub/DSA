def method1(ll: list, arr_size: int, sum: int) -> int:
    s = set()
    for i in range(0, arr_size):
        temp = sum - ll[i]
        if temp in s:
            print(
                "Pair with given sum "
                + str(sum)
                + " is ("
                + str(ll[i])
                + ", "
                + str(temp)
                + ")"
                + s.add(ll[i])
            )


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [1, 4, 45, 6, 10, 8]
    n = 16
    print(timeit(lambda: method1(ll, len(ll), n))) # 0.6651965910059516
    """
