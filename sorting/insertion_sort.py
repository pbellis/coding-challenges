def linear_search(arr, val):
	for i in range(len(arr)):
		if arr[i] <= val:
			return i
	return -1
		
def binary_search(arr, val):
	return binary_search_rec(arr, val, 0, len(arr) - 1) if arr else -1
	
def binary_search_iter(arr, val):
	lo, mid, hi = 0, 0, len(arr) - 1
	
	while lo <= hi:
		mid = lo + (hi - lo) // 2
		if arr[mid] < val:
			lo = mid + 1
		elif arr[mid] > val:
			hi = mid - 1
		else:
			break
			
	if mid < len(arr) and arr[mid] < val:
		return mid + 1
	else:
		return mid
	
def binary_search_rec(arr, val, lo, hi):
	mid = lo + (hi - lo) // 2
	if lo > hi:
		return mid
	elif arr[mid] > val:
		return binary_search_rec(arr, val, lo, mid-1)
	elif arr[mid] < val:
		return binary_search_rec(arr, val, mid+1, hi)
	else:
		return mid
	

def insertion_sort(arr):
	sorted_arr = []
	
	for i in range(len(arr)):
		j = binary_search(sorted_arr, arr[i]) + 1
		sorted_arr = sorted_arr[:j] + [arr[i]] + sorted_arr[j:]
	
	return sorted_arr

from random import randint

n = 1000

arr = [randint(0, 1000) for _ in range(n)]
my_sorted = insertion_sort(arr)
py_sorted = sorted(arr)

for i in range(n):
	if my_sorted[i] != py_sorted[i]:
		print("expected: " + str(py_sorted[i]) + " actual: " + str(my_sorted[i]))
