def sort_set(arr):
	for i in range(len(arr) - 1):
		indexToReplace = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[i]:
				indexToReplace = j
		arr[i], arr[indexToReplace] = arr[indexToReplace], arr[i]
	return arr