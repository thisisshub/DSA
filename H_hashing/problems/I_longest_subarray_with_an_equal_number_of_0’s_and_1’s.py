def method1(arr, n):
    hash_map = {}
    curr_sum = 0
    max_len = 0
    ending_index = -1

    for i in range(0, n):
        if arr[i] == 0:
            arr[i] = -1
        else:
            arr[i] = 1

    for i in range(0, n):
        curr_sum = curr_sum + arr[i]
        if curr_sum == 0:
            max_len = i + 1
            ending_index = i
        if curr_sum in hash_map:
            if max_len < i - hash_map[curr_sum]:
                max_len = i - hash_map[curr_sum]
                ending_index = i
        else:
            hash_map[curr_sum] = i

    for i in range(0, n):
        if arr[i] == -1:
            arr[i] = 0
        else:
            arr[i] = 1

    print(ending_index - max_len + 1, end=" ")
    print("to", end=" ")
    print(ending_index)

    return max_len


if __name__ == "__main__":
    
    from timeit import timeit
    arr = [1, 0, 0, 1, 0, 1, 1]
    n = len(arr)
    print(timeit(lambda: method1(arr, n), number=10000)) 
    
