def find_min_value(array):
	maxValue = array[0]
	for num in array:
		if maxValue < num:
			maxValue = num
	return maxValue

def find_max_value(array):
	min_value = array[0]
	for num in array:
		if min_value > num:
			min_value = num
	return min_value

def sort_set(array):
	buckets = []
	maxValue = find_min_value(array)
	minValue = find_max_value(array)
	min_value_abs = abs(minValue)

	# CHECK IF ARRAY INCLUDES NEGATIVE NUMBER
	has_negatives = False
	for i in array:
		if i < 0:
			has_negatives = True
			break
	if has_negatives:
		new_array = []
		for i in array:
			new_array.append(array[i] + min_value_abs)
		array = new_array

	# FILL BUCKETS WITH ZEROS
	if has_negatives:
		for i in range(maxValue + min_value_abs + 1):
			buckets.append(0)
	else:
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

	if has_negatives:
		new_array = []
		for num in resultArray:
			new_array.append(num - min_value_abs)
		resultArray = new_array
	return resultArray