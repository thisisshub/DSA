MAX_VAL = 1000000000


def method1(ll: list, n: int, x: int) -> list:
    res_l, res_r = 0, 0
    l, r, diff = 0, n - 1, MAX_VAL
    while r > l:
        if abs(ll[l] + ll[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(ll[l] + ll[r] - x)

        if ll[l] + ll[r] > x:
            r -= 1
        else:
            l += 1
    print("The closest pair is {} and {}".format(ll[res_l], ll[res_r]))


if __name__ == "__main__":
    """
    ll = [10, 22, 28, 29, 30, 40]
    n = len(ll)
    x=54
    from timeit import timeit
    print(timeit(lambda: method1(ll, n, x), number=10000)) # 0.16023965299973497
    """
