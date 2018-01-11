import pytest

import function

def func(a, b, c):
	def test():
		assert function.function(a, b) == c
	return test


test1 = func(30, 18, 6)
test2 = func(12, 50, 2)
