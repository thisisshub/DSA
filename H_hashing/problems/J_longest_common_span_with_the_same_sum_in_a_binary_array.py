def method1(ll1: list, ll2: list, n: int) -> int:
    maxLen = 0
    presum1 = presum2 = 0
    diff = {}
    for i in range(n):
        presum1 += ll1[i]
        presum2 += ll2[i]
        curr_diff = presum1 - presum2
        if curr_diff == 0:
            maxLen = i + 1
        elif curr_diff not in diff:
            diff[curr_diff] = i
        else:
            length = i - diff[curr_diff]
            maxLen = max(maxLen, length)

    return maxLen


if __name__ == "__main__":
    
    from timeit import timeit
    ll1 = [0, 1, 0, 1, 1, 1, 1]
    ll2 = [1, 1, 1, 1, 1, 0, 1]
    print(timeit(lambda: method1(ll1, ll2, len(ll1)), number=10000)) 
    
