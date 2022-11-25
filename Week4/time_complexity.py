# 1
"""
Time complexity is O(n^2). Every top level iteration in a given range
must undergo a subiteration in same range.
"""

def func(n): 
		for i in range(n):
				for j in range(n): 
						if j < i:
								break

# 2
"""
Time complexity is O(L*n). Every iteration of a v in L
must run a sub-function with O(n) complexity.

For instance, if L = 2, helper function will run twice.
helper_func(v) + helper_func(v)
O-Notation
O(n) + O(n)
2 * (O(n))
"""

def func(L):
		for v in L:
				# helper func time complexity is O(n)
				helper_func(v)


# 3
"""
(Assuming log base is 2...)
Time complexity is O(n(logn)). Top loop complexity determined by how many times
2 can divide into j before it is floored to 0 (2^x = n => log n = x).

Second loop's complexity is determined by the size of n. The bigger it is, the longer
it will take (linearly by addition and subtraction) for j to equal / exceed n.
"""
def func(n):
		j = n
		while j > 0:
				j = j // 2
		while j<n:
				j = j + 3
				n = n - 5
		return j

#4
"""
O(nlogn). Top loop T.C. is log(n). both sum and range methods are linear and dependent
on n. Each have complexity of O(n). Generating number range (O(n)) and summing its parts (O(n))
equates to two n's. By ignoring the constants, we get O(n*logn)
"""

def func(n):
		total = 0
		while n > 5:
				n = n // 2
				# Remember the time complexity of the sum and range methods
				total += sum(range(n))
		return total

#5
"""
O(n). Amount of calls linearly dependent on size of list declared with n.
The conditionals have no bearing on complexity.
"""

def func(n):
	for i in range(2,n):
			if n % i == 0:
					return True
			if i > n/i:
					return False

# 6
"""
O(n(n-1)). Each iteration of i (O(n)) will generate a list up to and not including i.
"""

def func(n):
		for i in range(n):
				for j in range(i):
						if j * j > I:
								break


# 7
"""
O(n). List size is linear
"""

def func(n):
    k=0
    for i in range(n//2, n): 
        j=1
        while (j <= n):
            k += 1
            j *= 2
    return k


# 8
"""
O(2^n). Each layer of fn contains two calls. Amount of layers dependent on n.
"""
def helper_func(x):
		for i in range(x): 
				print(i)
		return x

def func(n):
		if n == 2:
				return 0
		else:
				return helper_func(n - 1) + helper_func(n - 2)


# 9
"""
O(n^2). Amount of iterations is n^2. Print function is constant and has no bearing on complexity.
"""
def helper_func(n):
		for i in range(n**2):
		        print(i)
def func(n):
		for i in range(n**2): 
				print(helper_func(100))
		return 0