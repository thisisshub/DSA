def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)


def binomialCoeff(n, k):

    res = 1

    # Since C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k

    # Calculate value of [n*(n-1)*---*(n-k+1)] /
    # [k*(k-1)*---*1]
    for i in range(k):

        res *= n - i
        res //= i + 1

    return res


# A Binomial coefficient based function to
# find nth catalan number in O(n) time
def catalan(n):

    # Calculate value of 2nCn
    c = binomialCoeff(2 * n, n)

    # return 2nCn/(n+1)
    return c // (n + 1)


# A function to count number of BST
# with n nodes using catalan
def countBST(n):

    # find nth catalan number
    count = catalan(n)

    # return nth catalan number
    return count


# A function to count number of binary
# trees with n nodes
def countBT(n):

    # find count of BST with n numbers
    count = catalan(n)

    # return count * n!
    return count * factorial(n)


if __name__ == "__main__":
    """
    from timeit import timeit

    n = 5

    # find count of BST and binary
    # trees with n nodes
    count1 = countBST(n)
    count2 = countBT(n)

    # print count of BST and binary trees with n nodes
    print(timeit(lambda: count1, number=10000))  # 0.00043645999539876357
    print("Count of binary trees with", n, "nodes is", count2)
    """
