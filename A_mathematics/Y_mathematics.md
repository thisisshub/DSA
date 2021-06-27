
# Let's start with Mathematics 

## Count Digits
The first program we're gonna go through is called **Count Digits**. A very simple program where you count the number of digits a number has. You always do this in two ways,

1. Calculate the length of the integer after converting it into the string, keeping in mind to subtract 1 from the total length when the integer is negative 

```python
def  method1(n: int) -> int:
	"""
	>>> method1(0)
	1
	"""
	return  len(str(n)) if n >= 0  else  len(str(n)) - 1
```
2. By using the logarithm method where you calculate the log of the integer if it is positive otherwise you just calculate the negative log and add 1 at the end.
```python
def  method2(n: int) -> int:
	"""
	>>> method2(0)
	1
	"""
	import math
	return  int(math.log10(n) + 1  if n > 0  else (1  if n == 0  else math.log10(-n) + 1))
```

## Palindrome 

The second thing is palindrome. It is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as "madam" or 1221. To check if the given input is palindrome, we have a simple program.

1. We just reverse the input by [::-1] (courtesy of python) and check if it's equal to the original input.
```python 
def  method1(n: str) -> bool:
	"""
	>>> method1("1221")
	True
	"""
	return True if n == n[::-1] else False
```

 ## GCD (Greatest common divisor)
 
Third topic for the day is **Greatest common divisor** (**GCD**). For two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. We can do this two ways in python,

1. We use Euclidean Algorithm.
```python
def method1(n: int, m: int) -> int:
	"""
	>>> method1(4, 8)
	4
	"""
	while m:
		n, m = m, n % m
	return n
```
2.  We use the math module
```python
def method1(n: int, m: int) -> int:
	"""
	>>> method1(4, 8)
	4
	"""
	from math import gcd
	return gcd(n, m)
```
## Lcm 

The fourth topic is LCM, as you would expect. Once again we can go about writing this thing in two ways,

1. We do things mathematically calculating the gcd the euclidean way and then using it as a divisor to divide the product of our inputs. 
```python
def method(n: int, m: int) -> int:
	"""
	>>> method(2, 5)
	10
	"""
	def gcd(n, m):
		while m:
			n, m = m, n % m
		return n
	return abs(n * m) // gcd(n, m))
```

2. We can use the math module to calculate gcd and then use the same method as above.
```python
def method(n: int, m: int) -> int:
	"""
	>>> method(2, 4)
	4
	"""
	from math import gcd
	return abs(n * m) // gcd(n, m)
```

## Sieve of Eratosthenes
It is one of most widely used algorithms to find the prime numbers up to the range of given number.
Prime numbers are numbers that are divisible just by 1 or themselves. Note: 1 is not a prime number and 2 is the smallest even prime number
```python
def method(n: int) -> list:
	"""
	>>> method(10)
	[2, 3, 5, 7]
	"""
	if n <= 2:
		return []
	else:
		sieve = [True] * (n + 1)
		for x in range(3, int(n ** 0.5) + 1, 2):
			for y in range(3, (n // x) + 1, 2):
				sieve[(x * y)] = False
	return [2] + [i for i in range(3, n, 2) if sieve[i]]
```

## Factorial
Next we write the problem for factorial of a number. Factorial is a function that multiplies a number by every number below it till it reaches 1. Note: 0! = 1

```python
def method(n: int) -> int:
	"""
	>>> method(4)
	24
	"""
	return 1 if n == 1 or n == 0 else n * method(n - 1)
```

## Prime factors
Finally to finish the basics of the mathematics we have prime factors. Prime factors are the numbers that are factors of a number but are themselves prime numbers. It's a 2 step process in python to find them,

1. You pick out all the numbers till the square root of the input that divide the required input and put them in a list. 
2. Pick a number from divisors list and then start dividing this number by every other number in the list keeping in mind that the second number isn't equal to the one our algorithm picked out. If that number isn't divided then it is surely a prime number and hence a prime factor.


Example: We have divisors = [2, 3, 4, 6,] for 12. Algorithm then picks divisors[0] and starts dividing it with divisors[1], divisors[2], divisors[3] which returns True since every division fails. This goes on with the rest of the numbers as well and surely 4, 6 are removed and we are left with [2, 3] as prime factors for 12.

```python
def method(n: int) -> int:
	"""
	>>> method(12)
	[2, 3]
	"""
	divisors = [d for d in range(2, n // 2 + 1) if n % d == 0]
	return [d for d in divisors if all(d % od != 0 for od in divisors if od != d)]
```

Next Topic: - [Bits Set](https://github.com/thisisshub/DSA/blob/main/B_bit_magic/Z_bit_magic.md)