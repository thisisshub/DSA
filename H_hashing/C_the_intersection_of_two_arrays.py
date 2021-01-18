def method1(ll1, ll2, n1, n2):
    hs = set()
    for i in range(0, n1):
        hs.add(ll1[i])
    print("Intersection:")
    for i in range(0, n2):
        if ll2[i] in hs:
            print(ll2[i], end=" ")


if __name__ == "__main__":
    """
    from timeit import timeit
    ll1 = [7, 1, 5, 2, 3, 6]
    ll2 = [3, 8, 6, 20, 7]
    n1 = len(ll1)
    n2 = len(ll2)
    print(timeit(lambda: method1(ll1, ll2, n1, n2), number=10000)) # 0.11873356500291266
    """
