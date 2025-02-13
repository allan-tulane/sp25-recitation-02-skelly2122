"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	if n <= 1:  # Base case: if n is less than or equal to 1
			return 1  # Return 1 for the base case
	# Recursive case: calculate W(n) using the recurrence relation
	return a * simple_work_calc(n // b, a, b) + n  # Combine results of subproblems with the current work

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
				 the work done at each node 

	Returns: the value of W(n).
	"""
	if n <= 1:  # Base case: if n is less than or equal to 1
			return 1  # Return 1 for the base case
	# Recursive case: calculate W(n) using the recurrence relation with function f
	return a * work_calc(n // b, a, b, f) + f(n)  # Combine results of subproblems with f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence S(n) = S(n/b) + f(n)
	Note: for span, we take the maximum of recursive calls + f(n)
	"""
	if n <= 1:  # Base case: if n is less than or equal to 1
			return 1  # Return 1 for the base case
	# Recursive case: calculate the max span of the recursive calls and add current work f(n)
	return max(span_calc(n // b, a, b, f) for _ in range(a)) + f(n)  # Take max of span from all branches
def compare_work(work_fn1,
                 work_fn2,
                 sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((n, work_fn1(n), work_fn2(n)))
	return result


def print_results(results):
	""" done """
	print(
	    tabulate.tabulate(results,
	                      headers=['n', 'W_1', 'W_2'],
	                      floatfmt=".3f",
	                      tablefmt="github"))


def compare_span(span_fn1,
                 span_fn2,
                 sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((n, span_fn1(n), span_fn2(n)))
	return result
