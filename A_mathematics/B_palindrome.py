def method1(n: str) -> bool:
    '''Checks for palindrome by reversing the string'''

    return True if n == n[::-1] else False


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1('aibohphobia'), number=10000))
    """
