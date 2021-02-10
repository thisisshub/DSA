def method1(ll, n):

    max_so_far = 0
    max_ending_here = 0

    for i in range(0, n):
        max_ending_here = max_ending_here + ll[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


if __name__ == "__main__":
    
    ll = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    n = len(ll)
    from timeit import timeit
    print(timeit(lambda: method1(ll, n), number=10000)) 
    
