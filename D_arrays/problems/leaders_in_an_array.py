def method1():
    def method(ll: list, size: int) -> int:
        max_from_right = ll[size - 1]
        for i in range(size - 2, -1, -1):
            if max_from_right <= ll[i]:
                print(ll[i])
                max_from_right = ll[i]

    ll = [16, 17, 4, 3, 5, 2]
    return method(ll, len(ll))


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) # 0.08483552300003794
    """
