def method1(s: str) -> bool:
    return True if s == s[::-1] else False


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1("AABAA"), number=10000)) 
    
