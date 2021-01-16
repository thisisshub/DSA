def method1(ll: list) -> int:
    inversionCount = 0
    for i in range(len(ll) - 1):
        for j in range(i + 1, len(ll)):
            if ll[i] > ll[j]:
                inversionCount = inversionCount + 1

    return inversionCount


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [1, 9, 6, 4, 5]
    print(timeit(lambda: method1(ll), number=10000)) # 0.017585102999873925
    """
