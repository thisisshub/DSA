def method1(ll: list, n: int, sum: int) -> list:
    ll.sort()
    for i in range(0, n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            if ll[i] + ll[l] + ll[r] == sum:
                print("Triplet is", ll[i], ", ", ll[l], ", ", ll[r])
                return True
            elif ll[i] + ll[l] + ll[r] < sum:
                l += 1
            else:
                r -= 1
    return False


if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [1, 4, 45, 6, 10, 8]
    sum = 22
    n = len(ll)
    print(timeit(lambda: method1(ll, n, sum), number=10000)) # 0.13895291699918744
    """
