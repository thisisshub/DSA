def method1(ll: list, n: int, prefixSum: int) -> int: 
    prefixSum[0] = ll[0] 
    for i in range(1, n): 
        prefixSum[i] = prefixSum[i - 1] + ll[i] 

ll =[10, 4, 16, 20 ] 
n = len(ll) 
    
prefixSum = [0 for i in range(n + 1)] 
  
method1(ll, n, prefixSum) 

if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(ll, n, prefixSum), number=10000)) # 0.005700344998331275
    """