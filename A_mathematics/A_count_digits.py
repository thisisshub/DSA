def method1(n: int) -> int:
    '''Return the length of the string

    convert the integer to a string and get the length of the string.
    '''
    return len(str(abs(n)))  # ‘abs’ is used to handle the case even if the number is negative.


def method2(n: int) -> int:
    '''Return th length by math.log10() function

    Add 1 to the result obtained by math.log() because the log of any number
    is 1 less than the number of digits inside that number.
    '''
    import math

    return int(math.log10(n) + 1 if n > 0 else (1 if n == 0 else math.log10(-n) + 1))


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(1234567890), number=10000)) # 0.0022839140001451597
    print(timeit(lambda: method2(1234567890), number=10000)) # 0.004222848001518287
    """
