island = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]

def water_capacity(island):
	boundaries = []
	
	start = 0
	for i in range(start + 1, len(island)):
		if island[i] >= island[start]:
			boundaries.append((start, i))
			start = i
	end = start - 1
	start = len(island) - 1
	for i in range(start - 1, end, -1):
		if island[i] >= island[start]:
			boundaries.append((i, start))
			start = i
			
	capacity = 0
	for start, end in boundaries:
		height = min(island[start], island[end])
		for i in range(start+1, end):
			capacity += height - island[i]
			
	return capacity
