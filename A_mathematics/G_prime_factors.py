def method1(n: int) -> int:
    '''Return a list of prime factors of an integer by
    first checking if the modulo of the value of d and number is equal to 0.
    Then applying the for loop inside the for loop to count a factor only once.
    '''

    divisors = [d for d in range(2, n // 2 + 1) if n % d == 0]
    return [d for d in divisors if all(d % od != 0 for od in divisors if od != d)]


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(20), number=10000)) # 0.028740440000547096
    """
