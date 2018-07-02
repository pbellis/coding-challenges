# Notes
# Code is simplified, to avoid overhead of copying use pointers

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	else:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]
		return merge(merge_sort(left), merge_sort(right))
	
def merge(left, right):
	i, j = 0, 0
	
	arr = []
	
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr.append(left[i])
			i += 1
		else:
			arr.append(right[j])
			j += 1
	
	while i < len(left):
		arr.append(left[i])
		i += 1
		
	while j < len(right):
		arr.append(right[j])
		j += 1
		
	return arr
	
from random import randint

n = 1000

arr = [randint(0, 1000) for _ in range(n)]
my_sorted = merge_sort(arr)
py_sorted = sorted(arr)

for i in range(n):
	if my_sorted[i] != py_sorted[i]:
		print("expected: " + str(py_sorted[i]) + " actual: " + str(my_sorted[i]))
