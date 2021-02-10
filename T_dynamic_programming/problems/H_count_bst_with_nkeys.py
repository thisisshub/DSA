def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)


def binomialCoeff(n, k):

    res = 1

    
    if k > n - k:
        k = n - k

    
    
    for i in range(k):

        res *= n - i
        res //= i + 1

    return res




def catalan(n):

    
    c = binomialCoeff(2 * n, n)

    
    return c // (n + 1)




def countBST(n):

    
    count = catalan(n)

    
    return count




def countBT(n):

    
    count = catalan(n)

    
    return count * factorial(n)


if __name__ == "__main__":
    
    from timeit import timeit

    n = 5

    
    
    count1 = countBST(n)
    count2 = countBT(n)

    
    print(timeit(lambda: count1, number=10000))  
    print("Count of binary trees with", n, "nodes is", count2)
    
