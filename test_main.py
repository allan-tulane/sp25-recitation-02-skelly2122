from main import *


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36  # when n=10, a=2, b=2
	assert simple_work_calc(20, 3, 2) == 230  # when n=20, a=3, b=2
	assert simple_work_calc(30, 4, 2) == 650  # when n=30, a=4, b=2
	assert simple_work_calc(8, 2, 2) == 32  # additional test case
	assert simple_work_calc(16, 2, 2) == 80  # additional test case
	assert simple_work_calc(24, 3, 2) == 276  # additional test case


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n * n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(8, 2, 2, lambda n: n // 2) == 20
	assert work_calc(16, 2, 2, lambda n: n + 1) == 95
	assert work_calc(24, 1, 3, lambda n: n) == 35


def test_asymptotic():
	# Test f(n) = 1
	def work_fn1(n):
		return work_calc(n, 2, 2, lambda n: 1)
	
	# Test f(n) = log n
	def work_fn2(n):
		return work_calc(n, 2, 2, lambda n: math.log2(n))
	
	# Test f(n) = n
	def work_fn3(n):
		return work_calc(n, 2, 2, lambda n: n)
	
	res = compare_work(work_fn1, work_fn2, sizes=[10, 20, 40, 80, 160, 320])
	print("\nComparing f(n)=1 vs f(n)=log n")
	print_results(res)
	
	res = compare_work(work_fn2, work_fn3, sizes=[10, 20, 40, 80, 160, 320])
	print("\nComparing f(n)=log n vs f(n)=n")
	print_results(res)

def test_compare_work():
	# Test cases where a=4, b=2
	# log_b(a) = log_2(4) = 2
	
	# Case 1: c < log_b(a) (c=1)
	def work_fn1(n):
		return work_calc(n, 4, 2, lambda x: x)
	
	# Case 2: c = log_b(a) (c=2)
	def work_fn2(n):
		return work_calc(n, 4, 2, lambda x: x**2)
	
	# Case 3: c > log_b(a) (c=3)
	def work_fn3(n):
		return work_calc(n, 4, 2, lambda x: x**3)
	
	print("\nComparing c < log_b(a) vs c = log_b(a)")
	res = compare_work(work_fn1, work_fn2, sizes=[10, 20, 40, 80])
	print_results(res)
	
	print("\nComparing c = log_b(a) vs c > log_b(a)")
	res = compare_work(work_fn2, work_fn3, sizes=[10, 20, 40, 80])
	print_results(res)


def test_compare_span():
    # Test with f(n) = 1
    def span_fn1(n):
        return span_calc(n, 2, 2, lambda n: 1)
    
    # Test with f(n) = log n
    def span_fn2(n):
        return span_calc(n, 2, 2, lambda n: math.log2(n))
    
    # Test with f(n) = n
    def span_fn3(n):
        return span_calc(n, 2, 2, lambda n: n)
    
    print("\nComparing span with f(n)=1 vs f(n)=log n")
    res = compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100])
    print_results(res)
    
    print("\nComparing span with f(n)=log n vs f(n)=n")
    res = compare_span(span_fn2, span_fn3, sizes=[10, 20, 50, 100])
    print_results(res)
