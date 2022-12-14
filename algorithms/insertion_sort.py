def sort_set(array):
	for borderIndex in range(1, len(array)):
		itemToInsertValue = array[borderIndex]
		i = borderIndex - 1
		while i >= 0 and array[i] > itemToInsertValue:
			array[i + 1] = array[i]
			i -= 1
		array[i + 1] = itemToInsertValue
	return array