def naive_maximum_subarray(arr):
	bi, bj = -1, -1
	max_delta = -1
	
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			delta = arr[j] - arr[i]
			if delta > max_delta:
				bi, bj = i, j
				max_delta = delta
	return bi, bj, max_delta

def maximum_subarray(arr):
	deltas = [y - x for x, y in zip(arr, arr[1:])]
	lo, hi, sum = maximum_subarray_rec(deltas, 0, len(deltas) - 1)
	return lo, hi + 1, sum

def find_max_crossing_subarray(deltas, lo, mid, hi):
	max_left = -1
	left_sum = -1
	sum = 0
	for i in range(mid, lo-1, -1):
		sum += deltas[i]
		if sum > left_sum:
			left_sum = sum
			max_left = i
	max_right = -1
	right_sum = -1
	sum = 0
	for i in range(mid + 1, hi + 1):
		sum += deltas[i]
		if sum > right_sum:
			right_sum = sum
			max_right = i
	return max_left, max_right, left_sum + right_sum
	
def maximum_subarray_rec(deltas, lo, hi):
	if lo == hi:
		return lo, hi, deltas[lo]
	else:
		mid = lo + (hi - lo) // 2
		left = maximum_subarray_rec(deltas, lo, mid)
		right = maximum_subarray_rec(deltas, mid + 1, hi)
		cross = find_max_crossing_subarray(deltas, lo, mid, hi)
		return max((left, right, cross), key=lambda x: x[2])

if __name__ == "__main__":		
	print("running tests...")
	from random import randint
	for _ in range(10):
		arr = [randint(0, 99999) for _ in range(randint(100, 1000))]
		expected = naive_maximum_subarray(arr)
		actual = maximum_subarray(arr)
		if expected != actual:
			print("expected: ", expected)
			print("actual: ", actual)
			
	from timeit import Timer
	arr = [randint(0, 99999) for _ in range(1000)]
	print('naive: ', Timer(lambda: naive_maximum_subarray(arr)).timeit(100))
	print('d&c: ', Timer(lambda: maximum_subarray(arr)).timeit(100))
