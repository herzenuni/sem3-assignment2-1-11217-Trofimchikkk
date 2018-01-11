
import pytest 
import sort

def test_my_bs():
	res = [2,1,2,8,5,0,6]
	assert my_sort.bubble_sort(res) == sorted(res)

def test_my_qs():
	res = [2,1,2,8,5,0,6]
assert my_sort.quick_sort(res) == sorted(res)
