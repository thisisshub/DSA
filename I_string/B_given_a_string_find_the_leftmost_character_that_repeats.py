def method1(string: str) -> str:
    h = {}
    for i in string:
        if i in h:
            return i
        else:
            h[i] = 0
    return "\0"


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1("thisisastring"), number=10000)) # 0.0030865349999658065
    """
