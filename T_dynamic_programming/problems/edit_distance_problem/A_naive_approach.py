def method1(str1, str2, m, n):

    
    
    if m == 0:
        return n

    
    
    if n == 0:
        return m

    
    
    
    if str1[m - 1] == str2[n - 1]:
        return method1(str1, str2, m - 1, n - 1)

    
    
    
    
    return 1 + min(
        method1(str1, str2, m, n - 1),  
        method1(str1, str2, m - 1, n),  
        method1(str1, str2, m - 1, n - 1),  
    )


if __name__ == "__main__":
    
    from timeit import timeit

    
    str1 = "sunday"
    str2 = "saturday"
    print(
        timeit(lambda: method1(str1, str2, len(str1), len(str2)), number=10000)
    )  
    