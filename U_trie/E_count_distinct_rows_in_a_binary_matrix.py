def method1(s, m, n):

    # Initialize variable count that
    # stores the count of duplicate rows.
    i, j, count = 0, 0, 0

    # Take two nested loop and
    # check weather rows already
    # get seen then increment
    # count by 1 then break the loop.
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]:
                count += 1
                break

    # Check if count>=1 then prNo
    # Else prYes.
    if count >= 1:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    """
    from timeit import timeit

    m = 3
    n = 3
    s = [[1, 0, 1], [0, 0, 0], [1, 0, 0]]

    print(timeit(lambda: method1(s, m, n), number=10000))  # 0.04088545798731502
    """
