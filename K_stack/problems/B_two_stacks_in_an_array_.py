class TwoStacks: 
	
	def __init__(self, n):	 
		self.size = n 
		self.arr = [None] * n 
		self.top1 = -1
		self.top2 = self.size 
		
	
	def push1(self, x): 
		if self.top1 < self.top2 - 1 : 
			self.top1 = self.top1 + 1
			self.arr[self.top1] = x 
		else: 
			print("Stack Overflow ") 
			exit(1) 

	
	def push2(self, x): 
		if self.top1 < self.top2 - 1: 
			self.top2 = self.top2 - 1
			self.arr[self.top2] = x 
		else: 
			print("Stack Overflow ") 
			exit(1) 

	
	def pop1(self): 
		if self.top1 >= 0: 
			x = self.arr[self.top1] 
			self.top1 = self.top1 -1
			return x 
		else: 
			print("Stack Underflow ") 
			exit(1) 

	
	def pop2(self): 
		if self.top2 < self.size: 
			x = self.arr[self.top2] 
			self.top2 = self.top2 + 1
			return x 
		else: 
			print("Stack Underflow ") 
			exit() 


if __name__ == "__main__":\
	"""
	from timeit import timeit
	ts = TwoStacks(5) 
	ts.push1(1) 
	ts.push2(2) 
	ts.push2(3) 
	ts.push1(4) 
	ts.push2(5) 
	print(timeit(lambda: ts, number=10000)) # 0.0004057340011058841
	"""
