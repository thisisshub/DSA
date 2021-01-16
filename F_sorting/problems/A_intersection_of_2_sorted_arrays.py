def method1(ll1: list, ll2: list) -> list:
    ll = []
    for i in set(ll1):
        for j in set(ll2):
            if i == j:
                ll.append(i)
    return ll


def method2(ll1: list, ll2: list, m: int, n: int) -> int:
    i = j = 0
    while i < m and j < n:
        if ll1[i] < ll2[j]:
            i += 1
        elif ll2[j] < ll1[i]:
            j += 1
        else:
            print(ll2[j])
            j += 1
            i += 1


if __name__ == "__main__":
    """
    from timeit import timeit
    ll1 = [1, 2, 4, 5, 6]
    ll2 = [2, 3, 5, 7]
    m = len(ll1)
    n = len(ll2)
    print(timeit(lambda: method1(ll1, ll2), number=10000))  # 0.02140125900041312
    print(timeit(lambda: method2(ll1, ll2, m, n), number=10000))  # 0.06446200500067789
    """
