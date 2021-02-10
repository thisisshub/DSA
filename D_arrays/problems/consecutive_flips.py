def method1(s, n, k):
    cnt = 0
    prev = -1
    for i in range(0, k):
        if s[i] == "1":
            prev = i
    if prev == -1:
        cnt += 1
        prev = k - 1

    for i in range(k, n):
        if s[i] != "1":
            if prev <= (i - k):
                prev = i
                cnt += 1
        else:
            prev = i

    return cnt


s = "10000001"
n = len(s)
k = 2

if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(s, n, k), number=10000)) 
    
