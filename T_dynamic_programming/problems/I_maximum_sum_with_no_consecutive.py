def method1(arr):
    incl = 0
    excl = 0

    for i in arr:

        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return excl if excl > incl else incl


if __name__ == "__main__":
    """
    from timeit import timeit

    arr = [5, 5, 10, 100, 10, 5]
    print(timeit(lambda: method1(arr), number=10000))  # 0.003943671996239573
    """