def method_leftshift(n: int) -> bin:
    return bin(n << 2)


def method_rightshift(n: int) -> bin:
    return bin(n >> 2)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method_leftshift(60), number=10000)) # 0.0023728119999759656
    print(timeit(lambda: method_rightshift(60), number=10000)) # 0.0018800369998643873
    """
