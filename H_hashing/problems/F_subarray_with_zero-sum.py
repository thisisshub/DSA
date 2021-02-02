def method1(arr,n): 
	n_sum = 0
	s = set() 
	for i in range(n): 
		n_sum += arr[i] 
		if n_sum == 0 or n_sum in s: 
			return True
		s.add(n_sum) 
	return False

if __name__ == "__main__":
    """
    from timeit import timeit
    arr = [-3, 2, 3, 1, 6]	 
    n = len(arr) 
    print(timeit(lambda: method1(arr, n), number=10000)) # 0.01074043799599167
    """