def method1(str1, str2, m, n):

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return method1(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(
        method1(str1, str2, m, n - 1),  # Insert
        method1(str1, str2, m - 1, n),  # Remove
        method1(str1, str2, m - 1, n - 1),  # Replace
    )


if __name__ == "__main__":
    """
    from timeit import timeit

    # Driver code
    str1 = "sunday"
    str2 = "saturday"
    print(
        timeit(lambda: method1(str1, str2, len(str1), len(str2)), number=10000)
    )  # 0.2074630530041759
    """