from main import *


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36  # when n=10, a=2, b=2
	assert simple_work_calc(20, 3, 2) == 230  # when n=20, a=3, b=2
	assert simple_work_calc(30, 4, 2) == 650  # when n=30, a=4, b=2
	assert simple_work_calc(8, 2, 2) == 32  # additional test case
	assert simple_work_calc(16, 2, 2) == 80  # additional test case
	assert simple_work_calc(24, 3, 2) == 276  # additional test case


# def test_work():
# 	assert work_calc(10, 2, 2,lambda n: 1) == #TODO
# 	assert work_calc(20, 1, 2, lambda n: n*n) == #TODO
# 	assert work_calc(30, 3, 2, lambda n: n) == #TODO


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	res = compare_work(work_fn1, work_fn2)
	print(res)


def test_compare_span():
	# TODO
	pass
