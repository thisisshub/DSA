def method1(ll: list) -> list:
    from collections import Counter

    return sorted(ll, key=Counter(ll).get, reverse=True)


def method2(ll: list) -> list:
    return sorted(ll, key=ll.count, reverse=True)


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [1,2,3,4,3,3,3,6,7,1,1,9,3,2, 3, 2, 1, 3, 4, 5, 6, 7, 7, 7, 1]
    print(timeit(lambda: method1(ll), number=10000)) # 0.03473279799982265
    print(timeit(lambda: method2(ll), number=10000)) # 0.057430269999713346
    """
