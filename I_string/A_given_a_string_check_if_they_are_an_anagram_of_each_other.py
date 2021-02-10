def method1(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    str1 = sorted(s1)
    str2 = sorted(s2)

    for i in range(len(s1)):
        if str1[i] != str2[i]:
            return False
    return True


def method2(s1: str, s2: str) -> bool:
    count1 = [0] * 256
    count2 = [0] * 256
    for i in s1:
        count1[ord(i)] += 1
    for i in s2:
        count2[ord(i)] += 1

    if len(s1) != len(s2):
        return False
    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1("thisisastring", "stringthisisa"), number=10000)) 
    print(timeit(lambda: method2("thisisastring", "stringthisisa"), number=10000)) 
    
