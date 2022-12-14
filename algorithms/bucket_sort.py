def findMaxValue(array):
	maxValue = array[0]
	for num in array:
		if maxValue < num:
			maxValue = num
	return maxValue

def sort_set(array):
	buckets = []
	maxValue = findMaxValue(array)
	# FILL BUCKETS WITH ZEROS
	for i in range(maxValue + 1):
		buckets.append(0)

	# COUNT NUMBERS AND UPDATE ZEROS
	for i in range(len(array)):
		buckets[array[i]] += 1
	
	# FILL RESULT ARRAY 
	resultArray = []
	for i in range(len(buckets)):
		if buckets[i] != 0:
			for n in range(buckets[i]):
				resultArray.append(i)
	return resultArray