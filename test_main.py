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


def test_compare_work():
	# Create work functions using different f(n)
	def work_fn1(n):
		return work_calc(n, 2, 2, lambda x: x)
	
	def work_fn2(n):
		return work_calc(n, 2, 2, lambda x: x*x)
	
	res = compare_work(work_fn1, work_fn2)
	print_results(res)


def test_compare_span():
	def span_fn1(n):
		return span_calc(n, 2, 2, lambda x: x)
	
	def span_fn2(n):
		return span_calc(n, 2, 2, lambda x: x*x)
	
	res = compare_span(span_fn1, span_fn2)
	print_results(res)
