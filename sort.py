 def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr
    
def quick_sort(arr):
	if arr:
		head, *tail = arr
		return quick_sort([x for x in tail if x <= head]) + \
		[head] + \
		quick_sort([x for x in tail if x > head])
	return []

if __name__ == "__main__":

    import timeit

    print("TIMEIT")
    print("bubble_sort : ", end = '')
    print(timeit.timeit("bubble_sort([10,8,6,4,2,1,3,5,7,9])", setup = "from __main__ import bubble_sort", number = 100))
    print("quick_sort : ", end='')
print(timeit.timeit("quick_sort([10,8,6,4,2,1,3,5,7,9])", setup="from __main__ import quick_sort", number=100))
