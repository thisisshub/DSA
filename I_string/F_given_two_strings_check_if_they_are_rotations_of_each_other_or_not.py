def method1(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    temp = str1 + str2
    return True if temp.count(str2) else False


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1("ABCD", "DCBA"), number=10000)) 
    
